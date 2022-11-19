from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    SITES = (
        ("site1", ("Sydney")),
        ("site2", ("Melbourne")),
        ("site3", ("Adelaide")),
    )
    AVAILABLE_DATES = (
        ("date", (2006-10-25)),
    )
    TRIAL_STATUS = (
        ("Not_Taken", ("Not_Taken")),
        ("Approved", ("Approved")),
        ("Rejected", ("Rejected")),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    booked_user = models.BooleanField("User already booked a trial", default=False)
    booked_site = models.CharField("Booking Sites Available", max_length=32, choices=SITES, default="")
    booked_date = models.DateTimeField("Booking Dates Available", default=timezone.now)
    trial_status = models.CharField("Trial Status", max_length=32, choices=TRIAL_STATUS, default="Not_Taken")
    
    def __str__(self):
        return f'{self.user.username}'
