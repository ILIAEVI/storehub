from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from authentication.models import User
from store.models import Product


class UserCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        UserCart.objects.create(user=instance)
