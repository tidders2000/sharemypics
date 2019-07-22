from django.conf.urls import url, include
from .views import allPics

urlpatterns=[
    url(r'^$',allPics, name='allpics'),
    ]