from django import forms
from django.models import ModelForm
from . import Member


class MemberForm (ModelForm):
    
    class Meta:
        model = Member
        fields = '__all__'
