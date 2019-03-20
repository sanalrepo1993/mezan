from django.shortcuts import render

# Create your views here.
from . import models
from masjid.models import Masjid

def home(request):
    mazjis = Masjid.objects.all()
    context = {
        'mazjids':mazjis,
    }
    return render(request,'memebrs/home.html',context=context)
