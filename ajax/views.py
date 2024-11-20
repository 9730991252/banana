from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import *
from owner.models import *
from django.db.models import Q
# Create your views here.
def farmer_check(request):
    if request.method == 'GET':
        c = ''
        name = request.GET['name']
        address = request.GET['address']
        mobile = request.GET['mobile']
        shope_id = request.GET['shope_id']
        if 2 < len(name) :
            c = Farmer.objects.filter(Q(name__icontains=name),shope_id=shope_id)
        if 2 < len(address) :
            c = Farmer.objects.filter(Q(address__icontains=address),shope_id=shope_id)
        if 2 < len(mobile) :
            c = Farmer.objects.filter(Q(mobile__icontains=name),shope_id=shope_id)
        context={
            'c':c[0:3]
        }
        t = render_to_string('ajax/office/farmer_check.html', context)
    return JsonResponse({'t': t})