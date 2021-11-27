from django.contrib import admin

# Register your models here.
from .models import Customer, Vehicle, VehicleSize, VehicleType, RentalRate, Rental
admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(VehicleType)
admin.site.register(VehicleSize)
admin.site.register(Rental)
admin.site.register(RentalRate)



