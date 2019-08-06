from django.shortcuts import render, redirect, reverse
from cuspic.models import CusPic

# Create your views here.
""" passes list of events in the DB to the index page """
def index(request):
    events = CusPic.objects.values('event_name').distinct()
    
    return render(request, "index.html",{'events':events})