
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.cphh.models import Message, Inquiry



urlpatterns = [
    url(r'^', include('apps.cphh.urls', namespace='cphh')),
]
