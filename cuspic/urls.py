from django.conf.urls import url, include
from .views import allPics, SearchResultsView, add_an_image, my_images

urlpatterns=[
    url(r'^$',allPics, name='allpics'),
    url(r'^search/', SearchResultsView, name='search_results'),
    url(r'^add_image/', add_an_image, name='add_image'),
    url(r'^my_images/', my_images, name='my_images'),
    ]