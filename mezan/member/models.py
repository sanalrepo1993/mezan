from django.db import models

# Create your models here.

class Family(models.Model):
    house_name = models.CharField(unique = True,max_length = 100)
    house_address = models.TextField(max_length=500,null=True,)
    house_memebrship = models.IntegerField(null=True)
    def __str__(self):
        return self.house_name

class Member(models.Model):
    member_name = models.CharField (max_length = 100)
    member_contact_no = models.CharField (max_length = 15)
    member_dob = models.DateField (auto_now = False)
    member_email = models.CharField (max_length = 50)
    memeber_family = models.ForeignKey(Family,on_delete = models.CASCADE)
    def __str__(self):
        return self.member_name
    
