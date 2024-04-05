from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=255)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Floor(models.Model):
    name = models.CharField(max_length=255)
    svg = models.TextField(null = True, blank=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    department = models.ManyToManyField(Department, blank=True)
    floor_no = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.name + f"({self.building})"

class Place(models.Model):
    title = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    floor_name = models.ForeignKey(Floor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + f"({self.floor_name})"
    
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
class Visitor(models.Model):

    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.name