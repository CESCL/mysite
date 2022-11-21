from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from tempus_dominus.widgets import DatePicker, TimePicker

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField()
    first_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    SITES = (
        ("Sydney", ("Sydney")),
        ("Brisbaine", ("Brisbaine")),
        ("Adelaide", ("Adelaide")),
    )
    booked_site = forms.CharField(
        label='Select your trial site:',
        widget=forms.Select(choices=SITES)
    )
    booked_date = forms.DateField(
        label="Select your trial date:", 
        widget=DatePicker()
        )
    booked_time = forms.DateField(
        label="Select your trial time:", 
        widget=TimePicker(
            options={
                'format': 'HH:00',
                'disabledHours': [0, 1, 2, 3, 4, 5, 6, 7, 8, 18, 19, 20, 21, 22, 23, 24],
                'enabledHours': [9, 10, 11, 12, 13, 14, 15, 16],
            }
        )
    )
    class Meta:
        model = Profile
        fields = ['booked_site', 'booked_date', 'booked_time']