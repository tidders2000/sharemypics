from django.shortcuts import render, redirect, reverse

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")