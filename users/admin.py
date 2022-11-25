from django.contrib import admin
from .models import Booking, License

# Register your models here.

#admin.site.register(Booking)

@admin.register(Booking)
class BookedUsers(admin.ModelAdmin):
    list_display = ("user", "booked_user", "booked_date", "trial_status")

@admin.register(License)
class LicenseStatus(admin.ModelAdmin):
    list_display = ("user", "license_status")