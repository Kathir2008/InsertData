from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class data(models.Model):
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)