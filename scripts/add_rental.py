from rent.models import Customer, Vehicle, Rental
from faker import Faker
import random

fake = Faker()


def run():
    for i in range(45):
        rental_date = fake.date_between(start_date="-3y", end_date="now")
        while True:
            return_date = random.choices(population=[fake.date_between(start_date="-3y", end_date="now"),None], weights=[0.8,0.2], k=1)[0]
            print('return_date', return_date)
            if return_date is None:
                print('none')
                break
            elif return_date > rental_date:
                print('grd')
                break

        customers = Customer.objects.all()
        customer = random.choice(customers)

        vehicles = Vehicle.objects.all()
        while True:
            vehicle = random.choice(vehicles)
            print('vehicle', vehicle)
            if vehicle.rental_set.all():
                for rental in vehicle.rental_set.all():
                    if rental.return_date is not None:
                        if rental_date>rental.return_date:
                            break
                        else:
                            continue
            else:
                break
        print('done')
        Rental.objects.create(rental_date=rental_date, return_date=return_date, customer=customer, vehicle=vehicle)
