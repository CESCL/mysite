from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader
from .models import Applicant, Booking

def home(request):
    return render(request, "myapp/home.html")