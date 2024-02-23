from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=255)
    floor = models.IntegerField()

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)

    def __str__(self):
        return self.name