from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    floor = models.IntegerField()

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name