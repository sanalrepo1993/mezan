from django.db import models

# Create your models here.

class Canteen (models.Model):
    canteen_name = models.CharField (max_length = 100)
    canteen_contact_no = models.CharField (max_length = 15)
    
