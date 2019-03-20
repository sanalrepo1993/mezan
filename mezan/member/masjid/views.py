from django.shortcuts import render
from rest_framework import viewsets
from .models import Masjid
from .serializers import MasjidSerializer
from . import tablecontext
from .forms import MasjidForm
from django.shortcuts import redirect
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

def edit(request,id):
    masjid = Masjid.objects.get(id=id)
    if request.method == "POST":
        masjidform = MasjidForm(request.POST,instance=masjid)
        if masjidform.is_valid():
            masjidform.save()
        else:
            print(masjidform.errors)
    else:
        masjidform = MasjidForm(instance= masjid)

    context = {
            "form":masjidform,
            "formtitle":"Add new mazjid",
            "url":"/masjid/edit/"+str(id)
        }
    return render(request,"base/forms.html",context)

def delete(request,id):
    masjid = Masjid.objects.get(id=id)
    deleted = False
    if request.method == "POST":
        #masjidform = MasjidForm(data=request.POST,instance=masjid)
        masjid.delete()
        deleted = True
    else:
        masjidform = MasjidForm(instance= masjid)

        context = {
                "form":masjidform,
                "formtitle":"Delete mazjid",
                "url":"/masjid/delete/"+str(id),
                "delete_form": "true",
            }
    if deleted:
        return redirect('/masjid/',permanent=True)
    else:
        return render(request,"base/forms.html",context)

def details(request,id):
    data = Masjid.objects.get(id=id)
    context = {
        'data':data,
        'details':"Mazjid Details",
    }
    return render(request,'masjid/details.html',context)



class MasjidViewSet(viewsets.ModelViewSet):
    queryset = Masjid.objects.all()
    serializer_class = MasjidSerializer