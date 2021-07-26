from django.db import models

# Create your models here.
class login(models.Model):
    Name = models.CharField(max_length=100)
    age = models.IntegerField()
    Email =models.CharField(max_length=100)
    Password = models.CharField(max_length=100)