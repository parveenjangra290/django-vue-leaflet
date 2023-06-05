"""
    MapAPI URLs.
"""
from django.urls import path, include
from . import views
from rest_framework import routers
from mapapi.api import api

router = routers.SimpleRouter()
router.register('', api.FarmerAPIViewSet, basename='farmer-list')

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
]