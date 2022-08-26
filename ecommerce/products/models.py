from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField(max_length=40)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    stock = models.IntegerField()
    email = models.EmailField()

class Distributor(models.Model):
    name = models.CharField(max_length=40)
    zone = models.CharField(max_length=40)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    email = models.EmailField()

class Shop(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    email = models.EmailField()



