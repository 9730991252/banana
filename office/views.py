from django.shortcuts import render, redirect
from sunil.models import *
from owner.models import *
from django.views.decorators.csrf import csrf_exempt
import math
# Create your views here.
def office_home(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile).first()
        context={
            'e':e,
        }
        return render(request, 'office/office_home.html', context)
    else:
        return redirect('login')
    
@csrf_exempt
def new_farmer_bill(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile).first()
        selected_farmer_status = 0
        farmer = ''
        if 'add_farmer'in request.POST:
            name = request.POST.get('name')
            address = request.POST.get('address')
            c_mobile = request.POST.get('mobile')
            Farmer(
                shope_id=e.shope.id,
                name=name,
                address=address,
                mobile=c_mobile
            ).save()
            selected_farmer_status = 1
            farmer = Farmer.objects.filter(shope_id=e.shope.id).last()
        if 'select_farmer'in request.POST:
            fid = request.POST.get('farmer_id')
            selected_farmer_status = 1
            farmer = Farmer.objects.filter(id=fid).first()
        if 'complete_bill'in request.POST:
            farmer_id = request.POST.get('farmer_id')
            shope_id = e.shope.id
            vehicale_number = request.POST.get('vehicale_number')
            weight = request.POST.get('weight')
            empty_box = request.POST.get('empty_box')
            wasteage = request.POST.get('wasteage')
            prise = request.POST.get('prise')
            labor_amount = request.POST.get('labor')
            total_amount = request.POST.get('total_amount')
            bill_number = Farmer_bill.objects.filter(shope_id=shope_id).count()
            bill_number += 1
            Farmer_bill(
                farmer_id=farmer_id,
                shope_id=shope_id,
                office_employee_id=e.id,
                vehicale_number=vehicale_number,
                weight=weight,
                empty_box=empty_box,
                wasteage=wasteage,
                prise=prise,
                total_amount=total_amount,
                bill_number=bill_number,
                labor_amount=labor_amount
            ).save()
            f = Farmer_bill.objects.filter(shope_id=shope_id).last()
            return redirect(f'/office/view_farmer_bill/{f.id}')
        context={
            'e':e,
            'selected_farmer_status':selected_farmer_status,
            'farmer':farmer
        }
        return render(request, 'office/new_farmer_bill.html', context)
    else:
        return redirect('login')
    
def farmer_bill(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile).first()
        context={
            'e':e,
            'bill':Farmer_bill.objects.filter(shope_id=e.shope.id).order_by('-id')
        }
        return render(request, 'office/farmer_bill.html', context)
    else:
        return redirect('login')
    
def view_farmer_bill(request, id):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile).first()
        bill = Farmer_bill.objects.filter(id=id).first()
        empty_box_weight = (bill.weight - bill.empty_box)
        wasteage_weight = (empty_box_weight + bill.wasteage)
        danda_weight = (wasteage_weight / 100) * 8
        total_weight = (wasteage_weight + danda_weight)
        amount = (bill.prise * math.floor(total_weight))
        context={
            'e':e,
            'bill':bill,
            'empty_box_weight':empty_box_weight,
            'wasteage_weight':wasteage_weight,
            'danda_weight':danda_weight,
            'total_weight':total_weight,
            'amount':amount
        }
        return render(request, 'office/view_farmer_bill.html', context)
    else:
        return redirect('login')
    
def add_employee(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile).first()
        if e:
            if 'Add_employee'in request.POST:
                name = request.POST.get('name')
                mobile = request.POST.get('mobile')
                pin = request.POST.get('pin')
                if office_employee.objects.filter(mobile=mobile).exists():
                    pass
                else:
                    office_employee(
                        shope_id=e.shope.id,
                        name=name,
                        mobile=mobile,
                        pin=pin,
                    ).save()    
                return redirect('/owner/add_employee/')
            if 'Edit_employee'in request.POST:
                id = request.POST.get('id')
                name = request.POST.get('name')
                mobile = request.POST.get('mobile')
                pin = request.POST.get('pin')
                office_employee(
                    id=id,
                    shope_id=e.shope.id,
                    name=name,
                    mobile=mobile,
                    pin=pin,
                ).save()
                return redirect('/office/add_employee/')
            if 'active'in request.POST:
                id = request.POST.get('id')
                c = office_employee.objects.filter(id=id).first()
                c.status = 0
                c.save()
                return redirect('/office/add_employee/')
            if 'deactive'in request.POST:
                id = request.POST.get('id')
                c = office_employee.objects.filter(id=id).first()
                c.status = 1
                c.save()
                return redirect('/office/add_employee/')
            
        else:
            del request.session['office_mobile']
            return redirect('login')
        context={
            'e':e,
            'office_employee':office_employee.objects.filter(shope_id=e.shope.id)
        }
        return render(request, 'office/add_employee.html', context)
    else:
        return redirect('login')
    
def profile(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile).first()
        if e:
            if 'edit_profile'in request.POST:
                shope_name = request.POST.get('shope_name')
                owner_name = request.POST.get('owner_name')
                address = request.POST.get('address')
                description = request.POST.get('description')
                contact_details = request.POST.get('contact_details')
                e.shope.shope_name = shope_name
                e.shope.owner_name = owner_name
                e.shope.address = address
                e.shope.description = description
                e.shope.contact_details = contact_details
                e.shope.save()

        else:
            del request.session['office_mobile']
            
        context={
            'e':e
        }
        return render(request, 'office/profile.html', context)
    else:
        return redirect('login')
