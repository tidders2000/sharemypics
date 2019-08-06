from django.conf.urls import url
from .views import checkout, download_images

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^download_images',download_images, name='download_images')
]
