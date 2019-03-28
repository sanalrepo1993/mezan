from django.db import models

class IncomeTypes(models.Model):
    income_type = models.CharField(unique=True,max_length=100)

class ExpenseTypes(models.Model):
    expense_type = models.CharField(unique=True,max_length=100)

# Create your models here.
class Income(models.Model):
    details = models.CharField(max_length = 30)
    date = models.DateField(auto_now=False)
    type = models.ForeignKey(IncomeTypes,on_delete = models.CASCADE)
    amount = models.IntegerField(max_length=20)

class Expense(models.Model):
    details = models.CharField(max_length = 30)
    date = models.DateField(auto_now=False)
    type = models.ForeignKey(ExpenseTypes,on_delete = models.CASCADE)
    amount = models.IntegerField(max_length=20)