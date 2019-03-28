from django import forms
from . import models 

class IncomeTypesForm(forms.ModelForm):
    class Meta:
        model = models.IncomeTypes
        fields = '__all__'

class ExpenseTypesForm(forms.ModelForm):
    class Meta:
        model = models.ExpenseTypes
        fields = '__all__'

class IncomeForm (forms.ModelForm):
    
    class Meta:
        model = models.Income
        fields = '__all__'
        widgets  = { 'date' : forms.DateInput(attrs= {'type':'date'}), }  

class ExpenseForm (forms.ModelForm):
    
    class Meta:
        model = models.Expense
        fields = '__all__'
        widgets  = { 'date' : forms.DateInput(attrs= {'type':'date'}), } 