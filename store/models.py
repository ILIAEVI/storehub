import os
import uuid
from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from authentication.models import User


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
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=generate_image_path, null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='products')
    weight = models.PositiveIntegerField(default=0)
    country_of_origin = models.CharField(max_length=100)
    quality = models.CharField(max_length=100)
    healthy = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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