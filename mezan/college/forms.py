from django import forms
from .models import Colleage


class SchoolForm (forms.ModelForm):

    class Meta :
        models = Colleage
        fields = '__all__'

