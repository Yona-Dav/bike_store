from rent.models import Customer, Vehicle, Rental, VehicleSize,VehicleType
from faker import Faker
fake = Faker()

def run():
    for i in range(30):
        f = (fake.name()).split()[0]
        l =(fake.name()).split()[-1]
        e = fake.email()
        p = fake.country_calling.code()+fake.msisdn()
        a = fake.address()
        c = fake.city()
        co = fake.country()
        Customer.objects.create(first_name=f, last_name=l,email=e,phone_number=p,address=a,city=c,country=co)