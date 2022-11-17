from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Applicant(models.Model):
    applicant_id = models.AutoField(primary_key=True, editable=False)
    applicant_given_name = models.CharField(max_length=30)
    applicant_family_name = models.CharField(max_length=30)
    applicant_email = models.EmailField()
    
    def __str__(self):
        return "{} - {}".format(self.applicant_id, self.applicant_email)
    
class Booking(models.Model):
    SITES = (
        ("site1", ("Sydney")),
        ("site2", ("Melbourne")),
        ("site3", ("Adelaide")),
    )
    AVAILABLE_DATES = (
        ("date", (2006-10-25)),
    )
    booking_id = models.ForeignKey(Applicant, on_delete=models.RESTRICT)
    booking_site = models.CharField("Booking Site Available", max_length=32, choices=SITES, default="Sydney")
    booking_date = models.DateTimeField("Booking Dates Available", default=timezone.now)
    
    def __str__(self):
        return "{} - date {}".format(self.booking_id, self.booking_date)
    