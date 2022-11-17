from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Applicant(models.Model):
    applicant_id = models.AutoField(primary_key=True, editable=False,  default='0')
    applicant_given_name = models.CharField(max_length=30)
    applicant_family_name = models.CharField(max_length=30)
    applicant_email = models.EmailField()
    
    def __str__(self):
        return self.applicant_id
    
class Booking(models.Model):
    booking_id = models.ForeignKey(Applicant, on_delete=models.RESTRICT)
    booking_site = models.CharField(max_length=20)
    booking_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.booking_id