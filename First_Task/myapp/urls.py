
from django.urls import path
from .views import home
from .views import base
from .views import about

urlpatterns = [
    path('',home),
    path('base',base),
    path('about',about),
    
]
