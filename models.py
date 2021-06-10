from django.db import models
import jsonfield
# Create your models here.

class Supplier(models.Model):
    name=models.CharField(max_length=70, blank=False)
    email=models.EmailField(blank=False)
    phone=models.BigIntegerField()
    address=models.CharField(max_length=100)

class User(models.Model):
    name=models.CharField(max_length=50, blank=False)
    email=models.EmailField(blank=False)
    phone=models.BigIntegerField()
    address=models.CharField(max_length=100)

class Medicine(models.Model):
    name=models.CharField(max_length=100, blank=False)
    content=jsonfield.JSONField()
    category=models.CharField(max_length=50)
    expDate=models.DateField()
    price=models.IntegerField()
    supplier=models.ForeignKey(Supplier, null=True,on_delete=models.SET_NULL)
    stock=models.IntegerField()

class Order(models.Model):
    ordDate=models.DateField()
    userId=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    medId=models.ForeignKey(Medicine, null=True, on_delete=models.SET_NULL)
    quantity=models.IntegerField()
    price=models.FloatField()
