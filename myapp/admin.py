from django.contrib import admin

# Register your models here.

from .models import Applicant, Booking

admin.site.register(Applicant)
admin.site.register(Booking)