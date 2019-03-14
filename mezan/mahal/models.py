from django.db import models

# Create your models here.

class Mahal(models.Model):
    mahal_name = models.CharField(max_length = 100)
    