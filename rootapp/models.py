from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(null=True,blank=True)
    time=models.CharField(max_length=100)