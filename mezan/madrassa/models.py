from django.db import models

# Create your models here.

class Madrassa (models.Model):
    madrassa_name = models.CharField (max_length = 100)
    madrassa_address = models.TextField (max_length = 400)
    madrassa_contact_no = models.CharField (max_length = 15)
    madrassa_email = models.CharField (max_length = 50)