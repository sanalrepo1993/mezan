from django.shortcuts import render


from .forms import SchoolForm
# Create your views here.


def add(request):
    school_form = SchoolForm()
    context ={
        "form" : school_form,
        "formtitle":"Add new student"
    }
    return render(request,"base/forms.html",context)