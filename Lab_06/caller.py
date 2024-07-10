import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from datetime import date, timedelta, datetime

from main_app.models import Bird, Animal, Mammal, Reptile, ZooKeeper, Veterinarian, ZooDisplayAnimal

# Create queries within functions



# Animal.objects.create(name="Nemo1", species="Clo1wnfish", birth_date="2019-03-10", sound="Bubb7les")
# Mammal.objects.create(name="Fluffy2", species="Ora1ngutan", birth_date="2018-01-10", sound="Ch7omps", fur_color="Reddish-brown")
# Bird.objects.create(name="Robby3", species="Americ3an Robin", birth_date="2021-09-20", sound="Chi7rp", wing_span=29.50)
# Reptile.objects.create(name="Python", species="Ball Python", birth_date="2019-07-01", sound="Hiss", scale_type="Smooth")
#
# animals = Animal.objects.all()
# for a in animals:
#     print(f"{a.name}: {a.species}.")

##test code 02
#
# zookeeper = ZooKeeper.objects.create(first_name="Peter", last_name="Johnson", phone_number="0899524265", specialty="Mammals")
# mammal = Mammal.objects.get(name="Fluffy")
# zookeeper.managed_animals.add(mammal)
# veterinarian = Veterinarian.objects.create(first_name="Dr. Michael", last_name="Smith", phone_number="9876543210", license_number="VET12345")
#
# zookeeper_from_db = ZooKeeper.objects.first()
# print(f"{zookeeper_from_db.first_name} {zookeeper_from_db.last_name} is a ZooKeeper.")
#
# veterinarian_from_db = Veterinarian.objects.first()
# print(f"{veterinarian_from_db.first_name} {veterinarian_from_db.last_name} is a Veterinarian.")

# test 03
# is_proxy = ZooDisplayAnimal._meta.proxy
#
# if is_proxy:
#     print("ZooDisplayAnimal is a proxy model.")
# else:
#     print("ZooDisplayAnimal is not a proxy model.")

##test 04
# zookeeper = ZooKeeper(first_name="John", last_name="Doe", phone_number="0123456789", specialty="Fishes")
# zookeeper.full_clean()
# zookeeper.save()

##test 05

# all_animals_info = ZooDisplayAnimal.objects.all()
# for a in all_animals_info:
#     print(a.display_info())
#     print(a.is_endangered())

#
# lion_birth_date = date.today() - timedelta(days=731)
# lion = Mammal.objects.create(name="Simba", species="Lion", birth_date=lion_birth_date, sound="Roar", fur_color="Golden")
# print(f"The lion's age is {lion.age}.")
#
# snake_birth_date = date.today() - timedelta(days=30)
# snake = Reptile.objects.create(name="Kaa", species="Python", birth_date=snake_birth_date, sound="Hiss", scale_type="Scales")
# print(f"The snake's age is {snake.age}.")

