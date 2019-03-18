from django import forms
from .models import Mahal


class MahalForm (forms.ModelForm):
    
    class Meta:
        model = Mahal
        fields = '__all__'
        widgets ={
            'mahal_address': forms.Textarea(attrs={'data-autoresize':True, 'rows': 2}),
        }
