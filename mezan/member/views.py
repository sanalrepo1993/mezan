from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from masjid.models import Masjid

def home(request):
    mazjis = Masjid.objects.all()
    context = {
        'foreignKeys':mazjis,
        'keyId':'masjidId',
        'enableKeys':True,
        'keyname':"Mazjid",

    }
    return render(request,'memebrs/home.html',context=context)
