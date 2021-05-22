from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_lawyer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

class Lawyer(models.Model):
    GENDER_CHOICE = (('M','Male'),('F',"Female"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    designation = models.CharField(max_length=25,default='inter lawyer')
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE,default='M')
    city = models.CharField(max_length=25,default='lucknow')
    lawyertype =models.CharField(max_length=25,default='Criminal Lawyer')
    experience = models.FloatField(default=1,help_text='no of years as lawyer')

class Client(models.Model):
    GENDER_CHOICE = (('M','Male'),('F',"Female"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE,default='M')
    