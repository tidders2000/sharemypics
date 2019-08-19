from django.shortcuts import render
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.conf import settings
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
from .models import CusPic
from .forms import add_image_form


""" a view that returns all pictures in the db """

def watermark_text(input_image_path,output_image_path,text, pos):
        photo = Image.open(input_image_path)
 
        # make the image editable
        drawing = ImageDraw.Draw(photo)
 
        black = (189, 8, 12)
        font_type = ImageFont.truetype("cuspic/arial.ttf", 30)
        drawing.text(pos, text, fill=black, font=font_type)
        photo.show()
        photo.save(output_image_path)

def allPics(request):
    
        
        img = 'static/images/83.jpg'
        watermark_text(img, 'static/images/test5.jpg',text='www.mousevspython.com',pos=(1200, 1000))
        return render(request, 'allpics.html')
    
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