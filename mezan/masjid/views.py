from django.shortcuts import render
from rest_framework import viewsets
from .models import Masjid
from .serializers import MasjidSerializer
from . import tablecontext
# Create your views here.

def home(request):
    t_context = tablecontext.index()
    return render(request,"masjid/home.html",t_context)

def add(request):
    return render(request,"")




class MasjidViewSet(viewsets.ModelViewSet):
    queryset = Masjid.objects.all()
    serializer_class = MasjidSerializer