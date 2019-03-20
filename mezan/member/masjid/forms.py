from django import forms
from django.forms import ModelForm
from .models import Masjid

class MasjidForm (ModelForm):

    class Meta:
        model = Masjid
        fields = '__all__'
        widgets ={
            'masjid_address': forms.Textarea(attrs={'data-autoresize':True, 'rows': 2}),
        }

   
