from django import forms
from .models import Mahal


class MahalForms (forms.ModelForm):

    class Meta :
        model = Mahal
        fileds = '__all__'
