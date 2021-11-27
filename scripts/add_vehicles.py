from rent.models import Customer, Vehicle, Rental, VehicleSize,VehicleType
import random

def run():
    for i in range(40):
        vehicle_type = VehicleType.objects.all()
        v_t = random.choice(vehicle_type)
        price = random.randint(10000,100000)
        vehicle_s = VehicleSize.objects.all()
        v_s = random.choice(vehicle_s)
        Vehicle.objects.create(vehicle_type=v_t,real_cost=price,size=v_s)