from django.db import models

# Create your models here.
class CusPic (models.Model):
    event_name = models.CharField(max_length=254, default='')
    username = models.CharField(max_length=254, blank=True)
    uploader_id = models.CharField(max_length=8)
    image = models.ImageField(upload_to='media/images')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    info = models.TextField()
    
    def __str__(self):
        return self.event_name 