from django import forms
from .models import CusPic

class add_image_form(forms.ModelForm):
    class Meta:
         model = CusPic
         fields = ('image', 'price', 'info')
