from django.shortcuts import render
from cuspic.models import CusPic

# Create your views here.

def do_search(request):
    pics=CusPic.objects.filter(username__icontains=request.GET['q'])
    return render(request,'search.html',{"pics":pics})