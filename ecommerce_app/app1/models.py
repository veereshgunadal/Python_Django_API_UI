from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 64)
    price = models.FloatField()
    category = models.CharField(max_length = 64)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 64, unique=True)
    password = models.TextField()
