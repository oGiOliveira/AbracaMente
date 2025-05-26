from django.db import models

# Create your models here.
class Agendamento(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100) 
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, default='')
    mode = models.CharField(max_length=20, default='')
    date = models.CharField(max_length=20, default='')
    hour = models.CharField(max_length=20, default='')
    message = models.TextField()
