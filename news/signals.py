from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Author


@receiver(post_save, sender=Author)
def notify_user(sender, instance, created, **kwargs):
    pass
