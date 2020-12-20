from django.db import models
from django.http import HttpResponse

# Create your models here.

class signup(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(default='')
    Password = models.CharField(max_length=20)
    
class login(models.Model):
    Email = models.EmailField(default='')
    Password = models.CharField(max_length=20)