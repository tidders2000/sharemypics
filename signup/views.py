from django.shortcuts import render
from.forms import signupform
from .models import signup

# Create your views here.

def signups(request):
    
    Signupform=signupform()
    
    return render(request,'signup.html',{'signupform':Signupform})
    

