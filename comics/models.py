from django.db import models

# Create your models here.
class Comic(models.Model):
    title =  models.CharField(max_length=200)
    image =  models.ImageField(null=True, blank=True)
    onsaleDate = models.DateTimeField()
    
    
class Character(models.Model):
    name =  models.CharField(max_length=200, null=True)
    image =  models.ImageField(null=True, blank=True)
    appearances = models.IntegerField()
    