from django.shortcuts import render, get_list_or_404, redirect
from .models import *
from .forms import RentalForm, CustomerForm, VehicleForm

# Create your views here.

def all_rental(request):
    rental_unreturned = Rental.objects.filter(return_date=None)
    rental_returned = get_list_or_404(Rental, return_date__isnull=False)
    rental_returned.sort(key=lambda x:x.return_date)
    return render(request, 'all_rental.html', {'unreturned':rental_unreturned, 'returned':rental_returned})

def single_rental(request, rental_id):
    rental = Rental.objects.get(id=rental_id)
    return render(request, 'single_rental.html', {'rent': rental})

def add_rental(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rent = Rental.objects.create(**form.cleaned_data)
            return redirect('all_rental')
    if request.method == 'GET':
        form = RentalForm()
    return render(request, 'add_rental.html', {'form':form})

def single_customer(request, customer_id):
    cust = Customer.objects.get(id=customer_id)
    return render(request, 'single_customer.html', {'customer': cust})

def all_customers(request):
    customer = get_list_or_404(Customer, last_name__isnull=False)
    customer.sort(key=lambda x: x.last_name)
    return(render(request, 'all_customers.html', {'customer': customer}))

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            cust = Customer.objects.create(**form.cleaned_data)
            return redirect('all_customers')
    if request.method == 'GET':
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form':form})

def all_vehicles(request):
    group = [vehicle.vehicle_type.id for vehicle in Vehicle.objects.all()]
    group = set(group)
    dict_group = {}
    for type in group:
        vehicles = Vehicle.objects.filter(vehicle_type = type )
        type_name = vehicles[0].vehicle_type.name.upper()
        dict_group[type_name]=vehicles
    return render(request, 'all_vehicles.html', {'type':dict_group})

def single_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    return render(request, 'single_vehicle.html', {'vehicle': vehicle})

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = Vehicle.objects.create(**form.cleaned_data)
            return redirect('all_vehicles')
    if request.method == 'GET':
        form = VehicleForm()
    return render(request, 'add_vehicle.html', {'form':form})