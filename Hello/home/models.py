from django.db import models
from django.forms import DateField

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    description=models.TextField()
    date=models,DateField()

def __str__(self):
    return self.name
    
    