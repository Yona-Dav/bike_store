from django.urls import path
from . import views

urlpatterns = [
    path('rental/', views.all_rental, name='all_rental'),
    path('rental/<int:rental_id>/', views.single_rental, name='single_rental'),
    path('rental/add/', views.add_rental, name='add_rental'),
    path('customer/<int:customer_id>/', views.single_customer, name='single_customer'),
    path('customer/', views.all_customers, name='all_customers'),
    path('customer/add/', views.add_customer, name='add_customer'),
    path('vehicle/', views.all_vehicles, name='all_vehicles'),
    path('vehicle/<int:vehicle_id>/', views.single_vehicle, name='single_vehicle'),
    path('vehicle/add/', views.add_vehicle, name='add_vehicle'),
]