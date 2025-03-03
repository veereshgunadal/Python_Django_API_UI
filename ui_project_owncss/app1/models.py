from django.db import models

# Create your models here.

class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 64, unique=True)
    release_date = models.DateField()
    actor = models.CharField(max_length = 64)
    actress = models.CharField(max_length = 64)
    language = models.CharField(max_length = 64)
    rating = models.FloatField()
