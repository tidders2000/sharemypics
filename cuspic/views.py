from django.shortcuts import render
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.conf import settings

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
@login_required()
def add_an_image(request):
    user=request.user
    events = CusPic.objects.values('event_name').distinct()
  
  
    if request.method=="POST":
      
      image = add_image_form(request.POST, request.FILES)
      event= request.POST.get('q')
      if image.is_valid():
          img=image.save(commit=False)
          
          img.user=user
          img.event_name=event
          img.save()
          messages.error(request,event)
          messages.error(request, "saved")
    
    else:    

     image=add_image_form()
     

    return render(request, 'add_image.html', {'add_image':image, 'events':events},{'user':user})
    
@login_required()
def my_images(request):
    
    my_img=CusPic.objects.filter(user=request.user)
    
    return render(request,'my_images.html', {'my_img':my_img})