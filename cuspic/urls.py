from django.conf.urls import url, include
from .views import allPics, SearchResultsView, add_an_image

urlpatterns=[
    url(r'^$',allPics, name='allpics'),
    url(r'^search/', SearchResultsView, name='search_results'),
    url(r'^add_image/', add_an_image, name='add_image')
    ]