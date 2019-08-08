from django import forms
from .models import CusPic

class add_image_form(forms.Form):
    class Meta:
         model = CusPic
         fields = ['event_name', 'image', 'price', 'info']
