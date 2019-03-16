from django import forms
from .models import Mahal


class MahalForm (forms.ModelForm):
    
    class Meta:
        model = Mahal
        fields = '__all__'
