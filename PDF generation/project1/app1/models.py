from django.db import models

# Create your models here.

class Laptop(models.Model):
    lid=models.IntegerField()
    name=models.CharField(max_length=40)
    brand=models.CharField(max_length=40)
    ram=models.CharField(max_length=40)
    rom=models.CharField(max_length=40)
    hdd=models.CharField(max_length=40)
    ssd=models.CharField(max_length=40)
    price=models.FloatField()