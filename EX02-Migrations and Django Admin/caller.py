import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Person, Item, Smartphone
import django.db.models
import main_app.apps

# Create queries within functions

# def some():
#     psn_model = Person.objects.all()
#     for p in psn_model:
#         if p.age <= 12:
#             p.age_group = "Child"
#         elif p.age <= 17:
#             p.age_group = "Teen"
#         else:
#             p.age_group = "Adult"
#         p.save()
#     for p in psn_model:
#         print(p.age_group)
# some()

o = Person.objects.filter(name='bitko')
print(Person.objects.filter(name='bitko'))
print(o[0].age)


# def items_test_function():
#     for x in range(1, 130, +1):
#         it = Item(name=f"zzzzzzz {x}", price=25.6 + float(x), quantity=5 + x, rarity=f'rarity {x}')
#         it.save()
#     print(Item.objects.all().values())
#
#

def items_update():
    items = Item.objects.all()
    x = 1.60
    for item in items:
        item.price = 0.55 + item.id
        x += 1
        item.save()
items_update()


def smarthpones_update():
    for x in range(50):
        if x % 2 == 0:
            ph = Smartphone(brand=f"Nokia 33{x}")
        else:
            ph = Smartphone(brand=f"xi 1{x}")
        ph.save()
smarthpones_update()