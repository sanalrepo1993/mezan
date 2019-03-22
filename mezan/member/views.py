from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from masjid.models import Masjid
from .forms import FamilyForm,MemberForm

from .serializer import FamilySerializer
from .tablecontext import index

class FamilyViewSet(viewsets.ModelViewSet):
    queryset = models.Family.objects.all()
    serializer_class = FamilySerializer

def home(request):
    mazjis = Masjid.objects.all()
    context = index()
    return render(request,'members/home.html',context=context)

def add_family(request):
    narvbar = True
    if 'ui' in request.GET:
        narvbar = False
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
            "navbar":narvbar,
            "formtitle":"Add New Family",
            "url":"/members/add/family/"
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
            "navbar":True,
            "formtitle":"Add New Family Member",
            "url":"/members/family/add/"
        }
    return render(request,"members/membersform.html",context)

