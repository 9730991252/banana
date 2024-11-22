from django.urls import path
from . import views
urlpatterns = [
    path('office_home/', views.office_home , name='office_home'),
    path('new_farmer_bill/', views.new_farmer_bill, name='new_farmer_bill'),
    path('farmer_bill/', views.farmer_bill, name='farmer_bill'),
    path('view_farmer_bill/<int:id>', views.view_farmer_bill, name='view_farmer_bill'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('profile/', views.profile, name='profile'),
    path('signature/', views.signature, name='signature'),
]