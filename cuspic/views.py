from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.conf import settings
from django.contrib.auth.models import User
from .models import CusPic
from .forms import add_image_form


""" a view that returns all pictures in the db """
def allPics(request):
    allpics = CusPic.objects.all()
    return render(request, 'allpics.html',{"allpics":allpics})
    
""" a view that returns pictures filtered by event"""
def SearchResultsView(request):
    
    query = request.GET.get('q')
    pics = CusPic.objects.filter(event_name__icontains=query)
    return render(request, 'search_results.html',{"pics":pics})

""" a view that allows users to add images to the db"""

def add_an_image(request):
    
    if request.method=="POST":
    
      image = add_image_form(request.POST, request.FILES)
      image.save()

    
    else:    

     image=add_image_form()
  

    return render(request, 'add_image.html', {'add_image':image},)
