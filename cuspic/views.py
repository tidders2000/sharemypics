from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import CusPic

def allPics(request):
    allpics = CusPic.objects.all()
    return render(request, 'allpics.html',{"allpics":allpics})

def SearchResultsView(request):
    pics = CusPic.objects.filter(event_name__icontains='British')
    return render(request, 'search_results.html',{"pics":pics})
