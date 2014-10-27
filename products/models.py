from django.db import models

class Company(models.Model):

    def __unicode__(self):
        return self.name

    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="comp_images")

class ItemType(models.Model):
    def __unicode__(self):
        return self.name
    iid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    url = models.CharField(max_length=100)

class Product(models.Model):
    def __unicode__(self):
        return self.name
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to="prod_images")
    company = models.ForeignKey(Company)
    itemtype = models.ForeignKey(ItemType)




# Create your models here.
