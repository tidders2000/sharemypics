from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CusPic (models.Model):
    event_name = models.CharField(max_length=254, default='')
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    info = models.TextField()
    wm_image = models.ImageField(upload_to='media/images/watermarks',blank=True)
    
    def __str__(self):
        return self.event_name 