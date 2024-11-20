from django.shortcuts import render, redirect
from sunil.models import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def owner_home(request):
    if request.session.has_key('owner_mobile'):
        mobile = request.session['owner_mobile']
        shope = Shope.objects.filter(mobile=mobile).first()
        context={
            'shope':shope
        }
        return render(request, 'owner/owner_home.html', context)
    else:
        return redirect('login')
     
def add_employee(request):
    if request.session.has_key('owner_mobile'):
        mobile = request.session['owner_mobile']
        shope = Shope.objects.filter(mobile=mobile).first()
        if 'Add_employee'in request.POST:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            if office_employee.objects.filter(mobile=mobile).exists():
                pass
            else:
                office_employee(
                    shope_id=shope.id,
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
                shope_id=shope.id,
                name=name,
                mobile=mobile,
                pin=pin,
            ).save()
            return redirect('/owner/add_employee/')
        if 'active'in request.POST:
            id = request.POST.get('id')
            c = office_employee.objects.filter(id=id).first()
            c.status = 0
            c.save()
            return redirect('/owner/add_employee/')
        if 'deactive'in request.POST:
            id = request.POST.get('id')
            c = office_employee.objects.filter(id=id).first()
            c.status = 1
            c.save()
            return redirect('/owner/add_employee/')
        
        context={
            'shope':shope,
            'office_employee':office_employee.objects.filter(shope_id=shope.id)
        }
        return render(request, 'owner/add_employee.html', context)
    else:
        return redirect('login')
    
def profile(request):
    if request.session.has_key('owner_mobile'):
        mobile = request.session['owner_mobile']
        shope = Shope.objects.filter(mobile=mobile).first()
        if 'edit_profile'in request.POST:
            shope_name = request.POST.get('shope_name')
            owner_name = request.POST.get('owner_name')
            address = request.POST.get('address')
            description = request.POST.get('description')
            contact_details = request.POST.get('contact_details')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            shope.shope_name = shope_name
            shope.owner_name = owner_name
            shope.address = address
            shope.description = description
            shope.contact_details = contact_details
            shope.pin = pin
            shope.save()
        context={
            'shope':shope
        }
        return render(request, 'owner/profile.html', context)
    else:
        return redirect('login')
    
@csrf_exempt
def farmer_bill(request):
    if request.session.has_key('owner_mobile'):
        mobile = request.session['owner_mobile']
        shope = Shope.objects.filter(mobile=mobile).first()
        selected_farmer_status = 0
        farmer = ''
        if 'add_farmer'in request.POST:
            name = request.POST.get('name')
            address = request.POST.get('address')
            c_mobile = request.POST.get('mobile')
            Farmer(
                shope_id=shope.id,
                name=name,
                address=address,
                mobile=c_mobile
            ).save()
            selected_farmer_status = 1
            farmer = Farmer.objects.filter(shope_id=shope.id).last()
            return redirect('farmer_bill')
        if 'select_farmer'in request.POST:
            farmer_id = request.POST.get('farmer_id')
            selected_farmer_status = 1
            farmer = Farmer.objects.filter(id=farmer_id).first()
        context={
            'shope':shope,
            'selected_farmer_status':selected_farmer_status,
            'farmer':farmer
        }
        return render(request, 'owner/farmer_bill.html', context)
    else:
        return redirect('login')