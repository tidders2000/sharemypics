from django.conf.urls import url, include
from .views import allPics, SearchResultsView

urlpatterns=[
    url(r'^$',allPics, name='allpics'),
    url(r'^search/', SearchResultsView, name='search_results'),
    ]