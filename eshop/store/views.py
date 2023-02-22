from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    banners = Banner.objects.all()
    return render(request,'store/home.html',{})

    context ={
        'banners' : banners
    }

    return render(request,'store/home.html',context)
