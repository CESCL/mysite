from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Booking(models.Model):
    TRIAL_STATUS = (
        ("Not Taken", ("Not Taken")),
        ("Approved", ("Approved")),
        ("Rejected", ("Rejected")),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    booked_user = models.BooleanField("Booked trial", default=False)
    booked_site = models.CharField("Booking Site", max_length=32, default="")
    booked_date = models.DateField("Booking Date", default=timezone.now)
    booked_time = models.TimeField("Booking Time", default=timezone.now,)
    trial_status = models.CharField("Trial Status", max_length=32, choices=TRIAL_STATUS, default="Not Taken")
    
    def __str__(self):
        return f"{self.user.username}, {self.user.first_name}, {self.user.last_name}"
