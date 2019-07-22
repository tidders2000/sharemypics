from django.shortcuts import render
from .models import CusPic

def allPics(request):
    allpics = CusPic.objects.all()
    return render(request, 'allpics.html',{"allpics":allpics})

# Create your views here.
