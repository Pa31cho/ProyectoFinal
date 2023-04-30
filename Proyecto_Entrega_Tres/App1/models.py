from django.db import models

# Create your models here.
class producto(models.Model):
    nombre= models.CharField(max_length=40)
    cantidad= models.IntegerField()

class cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
  