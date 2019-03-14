from django.db import models

# Create your models here.

class Member(models.Model):
    member_name = models.CharField (max_leength = 100)
    member_address = models.TextField (max_length = 400)
    member_contact_no = models.CharField (max_length = 15)
    member_dob = models.DateField (auto_now = False)
    member_email = models.CharField (max_length = 50)
    
