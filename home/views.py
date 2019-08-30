from django.shortcuts import render, redirect, reverse
from cuspic.models import CusPic
from django.contrib import messages
from django.contrib import auth
import os
from signup.forms import signupform
from django.views.generic import TemplateView, ListView

# Create your views here.
""" passes list of events in the DB to the index page """
def index(request):
    
    events = CusPic.objects.values('event_name').distinct()
    Signupform=signupform()
    return render(request, "index.html", {'events':events,'signupform':Signupform})