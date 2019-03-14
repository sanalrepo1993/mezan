from django.db import models

# Create your models here.

class Colleage (models.Model):
    colleage_name = models.CharField (max_length = 100)
    colleage_address = models.TextField (max_length = 400)
    colleage_contact_no = models.CharField (max_length = 15)
    colleage_email = models.CharField (max_length = 50)