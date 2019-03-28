from django.db import models

# Create your models here.

class FunctionTypes(models.Model):
    function_type = models.CharField(max_length=30)

class Functions(models.Model):
    function_name = models.CharField(max_length = 30)
    function_date = models.DateField(auto_now=False)
    function_cost = models.IntegerField(null=True)