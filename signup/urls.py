from django.conf.urls import url, include

from .views import signups

urlpatterns=[
    url(r'^signup/',signups, name='signups'),
    
    ]