from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Author
from django.core.mail import mail_managers


@receiver(post_save, sender=Author)
def notify_user(sender, instance, created, **kwargs):
    pass
