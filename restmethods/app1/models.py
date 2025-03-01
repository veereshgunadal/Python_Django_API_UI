from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 64)
    roll_no = models.IntegerField()
    age = models.IntegerField()
    addr = models.CharField(max_length = 64)
    ph_no = models.IntegerField()
    department = models.CharField(max_length = 64)