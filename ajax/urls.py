from django.urls import path
from . import views
urlpatterns = [
    path('farmer_check/', views.farmer_check, name='farmer_check'),
]