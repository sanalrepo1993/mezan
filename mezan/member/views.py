from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from masjid.models import Masjid
from .forms import FamilyForm,MemberForm
from django.http import HttpResponse, HttpResponseRedirect
from .serializer import FamilySerializer
from .tablecontext import index

class FamilyViewSet(viewsets.ModelViewSet):
    queryset = models.Family.objects.all()
    serializer_class = FamilySerializer
    

def home(request):
    mazjis = Masjid.objects.all()
    context = index()
    return render(request,'members/home.html',context=context)

def family_member(request,id):
    family = models.Family.objects.get(id= id)
    if request.method == "POST":
        memeberform = MemberForm(request.POST)
        if memeberform.is_valid():
            temp_mem = memeberform.save(commit= False)
            temp_mem.memeber_family = family
            temp_mem.save()
    else:
        memeberform = MemberForm()
    members = models.Member.objects.filter(memeber_family = family)
    context = {
        'table':members,
        'form':memeberform,
        'members':members,
        'family':family,
        'family_id':id,
    }
    return render(request,'members/family-members.html',context=context)

def family_member_edit(request,id,rid):
    member = models.Member.objects.get(id=id)
    if request.method == "POST":
        memeberform = MemberForm(request.POST,instance=member)
        if memeberform.is_valid():
            memeberform.save()
            return HttpResponseRedirect('/members/family/members/'+str(rid))
    else:
        memeberform = MemberForm(instance=member)
    #members = models.Member.objects.filter(memeber_family = family)
    context = {
        
        'form':memeberform,
       
        
        'family_id':id,
        'formtitle':'Edit member data',
    }
    return render(request,'base/forms.html',context=context)

def details(request,id):
    data = models.Family.objects.get(id=id)
    context = {
        'data':data,
        'details':"Family Details",
        "navbar":True,
    }
    return render(request,'members/details.html',context)

def delete(request,id,rid):
    models.Member.objects.filter(id=id).delete()
    return HttpResponseRedirect('/members/family/members/'+str(rid))

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
            "formtitle":"Add New Family Member",
            "url":"/members/family/add/"
        }
    return render(request,"members/membersform.html",context)

