import os
import uuid
from django.db import models
from django.db.models.signals import pre_save, post_delete, post_save
from django.dispatch import receiver
from authentication.models import User
from versatileimagefield.fields import VersatileImageField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


def generate_image_path(instance, filename):
    unique_filename = f"{uuid.uuid4().hex}/{instance.name}"
    return os.path.join('images', unique_filename)


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_categories'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    quantity = models.PositiveIntegerField(default=0, verbose_name=_('Quantity'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    image = VersatileImageField(upload_to=generate_image_path, null=True, blank=True)
    weight = models.PositiveIntegerField(default=0)
    country_of_origin = models.CharField(max_length=100, verbose_name=_('Country_of_origin'))
    quality = models.CharField(max_length=100)
    healthy = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, related_name='products')
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                              validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name

    @property
    def discounted_price(self):
        discount_amount = (self.price * self.discount_percentage) / 100
        new_price = self.price - discount_amount
        return f"{new_price:.2f}"


class FeedBack(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedback')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback')
    rating = models.PositiveIntegerField(default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(pre_save, sender=Product)
def update_image_pre_save(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_product = Product.objects.get(pk=instance.pk)
        except Product.DoesNotExist:
            return

        if old_product.image and old_product.image != instance.image:
            if os.path.isfile(old_product.image.path):
                os.remove(old_product.image.path)


@receiver(post_delete, sender=Product)
def delete_image_from_dir_on_delete(sender, instance, **kwargs):
    try:
        if instance.image:
            instance.image.delete()
    except FileNotFoundError:
        pass
