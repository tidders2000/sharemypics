from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from .models import CusPic


def allPics(request):
    allpics = CusPic.objects.all()
    return render(request, 'allpics.html',{"allpics":allpics})

def SearchResultsView(request):
    
    query = request.GET.get('q')
    pics = CusPic.objects.filter(event_name__icontains=query)
    return render(request, 'search_results.html',{"pics":pics})
