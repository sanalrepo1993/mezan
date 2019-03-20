from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from masjid.models import Masjid
from .forms import FamilyForm,MemberForm

def home(request):
    mazjis = Masjid.objects.all()
    context = {
        'foreignKeys':mazjis,
        'keyId':'masjidId',
        'enableKeys':True,
        'keyname':"Mazjid",

    }
    return render(request,'memebrs/home.html',context=context)

def add_family(request):
    if request.method == "POST":
        masjidform = FamilyForm(request.POST)
        if masjidform.is_valid():
            masjidform.save()
        else:
            print(masjidform.errors)
    else:
        masjidform = FamilyForm()

    context = {
            "form":masjidform,
            "formtitle":"Add new Family",
            "url":"/members/family/add/"
        }
    return render(request,"base/forms.html",context)

def add_member(request):
    if request.method == "POST":
        masjidform = MemberForm(request.POST)
        if masjidform.is_valid():
            masjidform.save()
        else:
            print(masjidform.errors)
    else:
        masjidform = MemberForm()

    context = {
            "form":masjidform,
            "formtitle":"Add new Family",
            "url":"/members/family/add/"
        }
    return render(request,"base/forms.html",context)

