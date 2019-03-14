from django.db import models

# Create your models here.

class School (models.Model):
    school_name = models.CharField (max_length = 100)
    school_address = models.TextField (max_length = 400)
    school_contact_no = models.CharField (max_length = 15)
    school_email = models.CharField (max_length = 50)