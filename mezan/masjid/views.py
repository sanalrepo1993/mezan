from django.shortcuts import render
from rest_framework import viewsets
from .models import Masjid
from .serializers import MasjidSerializer
from . import tablecontext
from .forms import MasjidForm
# Create your views here.

def home(request):
    t_context = tablecontext.index()
    return render(request,"masjid/home.html",t_context)

def add(request):
    if request.method == "POST":
        masjidform = MasjidForm(request.POST)
        if masjidform.is_valid():
            masjidform.save()
        else:
            print(masjidform.errors)
    else:
        masjidform = MasjidForm()

    context = {
            "form":masjidform,
            "formtitle":"Add new mazjid",
            "url":"/masjid/add/"
        }
    return render(request,"base/forms.html",context)





class MasjidViewSet(viewsets.ModelViewSet):
    queryset = Masjid.objects.all()
    serializer_class = MasjidSerializer