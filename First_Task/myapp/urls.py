
from django.urls import path
from .views import home
from .views import base

urlpatterns = [
    path('',home),
    path('base',base),
    
]
