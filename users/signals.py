from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Booking, License

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Booking.objects.create(user=instance)
        License.objects.create(user=instance)