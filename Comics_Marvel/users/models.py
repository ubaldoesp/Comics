import email
from operator import mod
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    password= models.CharField(max_length=64)
    
    def __str__(self):
        return self.name, self.username
