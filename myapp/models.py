from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'
    
class Booking(models.Model):
    SITES = (
        ("site1", ("Sydney")),
        ("site2", ("Melbourne")),
        ("site3", ("Adelaide")),
    )
    AVAILABLE_DATES = (
        ("date", (2006-10-25)),
    )
    booking_site = models.CharField("Booking Site Available", max_length=32, choices=SITES, default="Sydney")
    booking_date = models.DateTimeField("Booking Dates Available", default=timezone.now)
    
    def __str__(self):
        return "{} - date {}".format(self.booking_id, self.booking_date)
    