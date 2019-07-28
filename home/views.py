from django.shortcuts import render, redirect, reverse
from cuspic.models import CusPic

# Create your views here.
def index(request):
    events = CusPic.objects.values('event_name').distinct()
    
    return render(request, "index.html",{'events':events})