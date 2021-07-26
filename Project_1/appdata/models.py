from django.db import models

# Create your models here.
class value(models.Model):
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
