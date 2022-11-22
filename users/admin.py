from django.contrib import admin
from .models import Booking

# Register your models here.

#admin.site.register(Booking)

@admin.register(Booking)
class BookedUsers(admin.ModelAdmin):
    list_display = ("user", "booked_user", "booked_date", "trial_status")