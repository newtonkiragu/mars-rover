"""URL patterns for access through REST API."""
from __future__ import unicode_literals
from django.conf.urls import url
from .views import PhotoView, RoverView

urlpatterns = [
    url(r'photos/(?P<pk>[0-9]+)$', PhotoView.as_view(), name='photo-detail'),
    url(r'rovers/(?P<pk>[0-9]+)$', RoverView.as_view(), name='rover-detail'),
]
