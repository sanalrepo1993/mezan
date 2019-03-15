from django.shortcuts import render

# Create your views here.


def dashboard(request):
    context = {
        "title":"Dashboard",
    }
    return render(request,"dashboard/dashboard.html",context)

def login(request):
    return render(request,"auth/login.html")