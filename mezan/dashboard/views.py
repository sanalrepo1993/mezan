from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request,"dashboard/dashboard.html")

def login(request):
    return render(request,"auth/login.html")