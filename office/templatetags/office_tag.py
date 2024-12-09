from django import template
from owner.models import *
from django.db.models import Avg, Sum, Min, Max
from math import *
import math
from datetime import date
register = template.Library()
@register.simple_tag()
def user_pending_bill_amount(user_id):
    if user_id:
        total_pending_amount = ''
        
        bill = Farmer_bill.objects.filter(office_employee_id=user_id).aggregate(Sum('total_amount'))
        total_pending_amount = bill['total_amount__sum']
        
        c = Farmer_cash_transition.objects.filter(office_employee_id=user_id).aggregate(Sum('amount'))
        cash = c['amount__sum']
        if cash:
            total_pending_amount -= cash
        
        p = Farmer_Phonepe_transition.objects.filter(office_employee_id=user_id).aggregate(Sum('amount'))
        phonepe = p['amount__sum']
        if phonepe:
            total_pending_amount -= phonepe
        
        b = Farmer_bank_transition.objects.filter(office_employee_id=user_id).aggregate(Sum('amount'))
        bank = b['amount__sum']
        if bank:
            total_pending_amount -= bank
        
        if total_pending_amount == None:
            return 0
        else:
            return total_pending_amount
        
@register.simple_tag()
def product_cost_net_weight(weight, empty_box):
    a = (weight - empty_box)
    return a

@register.simple_tag()
def stalk_net_weight(wasteage, weight, empty_box):
    a = (((int(wasteage) + int(weight) - int(empty_box)) / 100) * 8)
    return math.floor(a)
        
@register.inclusion_tag('inclusion_tag/office/pendding_completed_farmer_bill.html')
def pendding_completed_farmer_bill(farmer_id):
    if farmer_id:
        farmer_bill = Farmer_bill.objects.filter(farmer_id=farmer_id)
        total_amount = farmer_bill.aggregate(Sum('total_amount'))
        total_amount = total_amount['total_amount__sum']
        print(total_amount)