from django.shortcuts import render, redirect,reverse
from.forms import signupform
from .models import signup
from django.contrib import messages

# Create your views here.

def signups(request):
    
    Signupform=signupform()
    
    return render(request,'signup.html',{'signupform':Signupform})
    

def emailadd(request):
    
      if request.method=="POST":
        
        signup = signupform(request.POST)
        if signup.is_valid():
         signup.save(commit=False)
         
         signup.save
         messages.error(request, 'email added')
        return redirect(reverse('index'))