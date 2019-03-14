from django.db import models

# Create your models here.

class Mahal(models.Model):
    mahal_name = models.CharField(max_length = 100)
    mahal_address = models.TextField(max_length = 400)
    mahal_contact_no = models.CharField(max_length = 15)
    mahal_email = models.CharField(max_length = 100)
    mahal_wakab_no = models.CharField(max_length = 20)
    