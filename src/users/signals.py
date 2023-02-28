from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from users.models import CustomUser

@receiver(post_save, sender=CustomUser)
def send_user_creation_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome to our site',
            'Thank you for joining our site!',
            'from@example.com',
            [instance.email],
            fail_silently=False,
        )

@receiver(post_save, sender=CustomUser)
def send_user_update_email(sender, instance, **kwargs):
    send_mail(
        'Profile updated',
        'Your profile has been updated.',
        'from@example.com',
        [instance.email],
        fail_silently=False,
    )