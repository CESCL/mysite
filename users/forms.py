from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

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
    booked_site = forms.CharField(label='Select your trial site:')
    booked_date = forms.DateField(
        label="Select your trial date:", 
        widget=DatePicker()
        )
    class Meta:
        model = Profile
        fields = ['booked_site', 'booked_date']