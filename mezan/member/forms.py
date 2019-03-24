from django import forms
from .models import Member
from .models import Family


class MemberForm (forms.ModelForm):
    
    class Meta:
        model = Member
        exclude = ['memeber_family']
        widgets  = { 'member_dob' : forms.DateInput(attrs= {'type':'date'}), }  

class FamilyForm (forms.ModelForm):
    
    class Meta:
        model = Family
        fields = '__all__'
        widgets  = { 'house_address' :forms.Textarea(attrs= {'rows':'2'}),}  

