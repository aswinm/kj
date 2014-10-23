from django.db import models

class Company(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to="prod_images")


# Create your models here.
