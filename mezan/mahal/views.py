from django.shortcuts import render
from rest_framework import viewsets
from .models import Mahal
from .serializers import MahalSerializer
from . import tablecontext
from .forms import MahalForm
# Create your views here.

def home(request):
    mahalFrom = None
    if request.method == "POST":
        try:
            mahal = Mahal.objects.get(id=1)
            mahalFrom = MahalForm(request.POST,instance=mahal)
        except:
            mahalFrom = MahalForm(request.POST)
        if mahalFrom.is_valid():
            mahalFrom.save()
        else:
            print(mahalFrom.errors)
        context = {
            "form":mahalFrom,
            "navbar":True,
            "formtitle":"Edit Mahal details",
            "url":"/mahal/"
        }
        return render(request,"base/forms.html",context)
    else:
        mahalFrom = None
        try:
            mahal = Mahal.objects.get(id=1)
            mahalFrom = MahalForm(instance=mahal)
        except:
            print("mahal object not found")
            mahalFrom = MahalForm()
        context = {
            "form":mahalFrom,
            "navbar":True,
            "formtitle":"Edit Mahal details",
            "url":"/mahal/"
        }
        return render(request,"base/forms.html",context)

def edit(request):
    mform = MahalForm()
    return render(request,"")




class MahalViewSet(viewsets.ModelViewSet):
    queryset = Mahal.objects.all()
    serializer_class = MahalSerializer