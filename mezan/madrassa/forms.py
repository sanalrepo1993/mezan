from django import forms
from .models import Madrassa


class MadrassaForm (forms.ModelForm):

    class Meta :
        model = Madrassa
        fields = '__all__'