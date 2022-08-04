from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField(max_length=40)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    email = models.EmailField()
