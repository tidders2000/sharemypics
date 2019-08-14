from django.conf.urls import url
from .views import checkout, download_images, sales

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^download_images',download_images, name='download_images'),
    url(r'^sales',sales, name='sales')
]
