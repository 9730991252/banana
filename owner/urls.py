from django.urls import path
from . import views
urlpatterns = [
    path('owner_home/', views.owner_home, name='owner_home'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('profile/', views.profile, name='profile'),
    path('new_farmer_bill/', views.new_farmer_bill, name='new_farmer_bill'),
    path('farmer_bill/', views.farmer_bill, name='farmer_bill'),
    path('complete_view_bill/<int:id>', views.complete_view_bill, name='complete_view_bill'),
]