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