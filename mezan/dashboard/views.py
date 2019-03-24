from django.shortcuts import render

# Create your views here.
from masjid.models import Masjid
from member.models import Family,Member

def dashboard(request):
    masjid_count = Masjid.objects.all().count()
    family_count = Family.objects.all().count()
    member_count = Member.objects.all().count()
    context = {
        "title":"Dashboard",
        "navbar":True,
        "masjid_count":masjid_count,
        "family_count":family_count,
        "member_count":member_count,
    }
    return render(request,"dashboard/dashboard.html",context)

def login(request):
    return render(request,"auth/login.html")