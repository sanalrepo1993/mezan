from django import forms
from .models import Member


class MemberForm (forms.ModelForm):
    
    class Meta:
        model = Member
        fields = '__all__'
        widgets  = { 'member_dob' : forms.DateInput(attrs= {'type':'date'}),}  
