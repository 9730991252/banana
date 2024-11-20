from django.db import models
from sunil.models import *
# Create your models here.
class office_employee(models.Model):
    shope = models.ForeignKey(Shope,on_delete=models.PROTECT,null=True)
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    pin = models.IntegerField()
    status = models.IntegerField(default=1)
    
class Farmer(models.Model):
    shope = models.ForeignKey(Shope,on_delete=models.PROTECT,null=True)
    office_employee = models.ForeignKey(office_employee,on_delete=models.PROTECT,null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200 , null=True)
    mobile = models.IntegerField()
    
class Farmer_bill(models.Model):
    farmer = models.ForeignKey(Farmer,on_delete=models.PROTECT,null=True)
    office_employee = models.ForeignKey(office_employee,on_delete=models.PROTECT,null=True)
    shope = models.ForeignKey(Shope,on_delete=models.PROTECT,null=True)
    vehicale_number = models.CharField(max_length=100)
    weight = models.IntegerField()
    empty_box = models.IntegerField()
    wasteage = models.IntegerField()
    prise = models.FloatField()
    total_amount = models.FloatField()
    paid_status = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    bill_number = models.IntegerField(null=True)
    added_date = models.DateTimeField(auto_now_add=True)