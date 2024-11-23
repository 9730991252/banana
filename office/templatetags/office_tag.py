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
        bill = Farmer_bill.objects.filter(office_employee_id=user_id).aggregate(Sum('total_amount'))
        total_pending_amount = bill['total_amount__sum']
        
        c = Farmer_cash_transition.objects.filter(office_employee_id=user_id).aggregate(Sum('amount'))
        cash = c['amount__sum']
        total_pending_amount -= cash
        
        p = Farmer_Phonepe_transition.objects.filter(office_employee_id=user_id).aggregate(Sum('amount'))
        phonepe = p['amount__sum']
        total_pending_amount -= phonepe
        
        b = Farmer_bank_transition.objects.filter(office_employee_id=user_id).aggregate(Sum('amount'))
        bank = b['amount__sum']
        total_pending_amount -= bank
        
        if total_pending_amount == None:
            return 0
        else:
            return total_pending_amount