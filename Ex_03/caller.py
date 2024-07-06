import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


# Create queries within functions


def create_pet(name: str, species: str):
    pet_to_create = Pet(name=name, species=species)
    pet_to_create.save()
    return f"{pet_to_create.name} is a very cute {pet_to_create.species}!"

# print(create_pet('Buddy', 'Dog'))

def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    atfct_to_crt = Artifact(name=name, origin=origin,age=age, description=description, is_magical=is_magical)
    atfct_to_crt.save()
    return f"The artifact {atfct_to_crt.name} is {atfct_to_crt.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age >250:
        artifact.name = new_name
        artifact.save()
    # Artifact.objects.filter(is_magical=True, age__gt=250, pk=artifact.pk).update(name=new_name)

def delete_all_artifacts():
    Artifact.objects.all().delete()

#

# create_artifact("Ancient Sword","Lost Kingdom",500,"A legendary sword with a rich history", True)
# create_artifact("Crystal Amulet","Mystic Forest",300,"A magical amulet believed to bring good fortune", True)
# create_artifact("Stone Tablet","Ruined Temple",1000,"An ancient tablet covered in mysterious inscriptions", False)



# print(create_artifact("Ston3 Tablet","Ruined Temple",1000,"An ancient tablet covered in mysterious inscriptions", False))


# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# artifact_object = Artifact.objects.get(name='Ancient Sword')
# rename_artifact(artifact_object, 'Ancient Shield')
# print(artifact_object.name)

# def cr_loc(name, region, population, description, is_capital):
#     location_2_create = Location(name=name, region=region, population=population, description=description, is_capital=is_capital)
#     location_2_create.save()
#
# cr_loc("Sofia","Sofia Region", 1329000, "The capital of Bulgaria and the largest city in the country", False)
# cr_loc("Plovdiv","Plovdiv Region", 346942, "The second-largest city in Bulgaria with a rich historical heritage", False)
# cr_loc("Varna","Varna Region", 330486, "A city known for its sea breeze and beautiful beaches on the Black Sea", False)



def show_all_locations():
    all_locations = Location.objects.all().order_by("-pk")
    return ('\n'.join([f"{x.name} has a population of {x.population}!" for x in all_locations]))

# print(show_all_locations())

def new_capital():
    Location.objects.filter(id=1).update(is_capital=True)
    # a = Location.objects.all().first()
    # a.is_capital=True
    # a.save()

# print(new_capital())

def get_capitals():
    return  Location.objects.filter(is_capital=True).values("name")

#
# print(get_capitals())


def delete_first_location():
    Location.objects.first().delete()


# delete_first_location()

def car_upload(model, year, color, price):
    new_car = Car(model=model, year=year, color=color, price=price)
    new_car.save()
#
car_upload("Mercedes C63 AMG", 2019, "white",120000.00)
car_upload("Audi Q7 S line", 2023, "black",183900.00)
car_upload("Chevrolet Corvette", 2021, "dark grey",199999.00)



def apply_discount():
    cars = Car.objects.all()
    for car in cars:
        discount = sum(int(x) for x in str(car.year)) / 100
        car.price_with_discount = float(car.price) - (float(car.price)*discount)
        # print(car.price_with_discount)
        car.save()


def get_recent_cars():
    recent_cars = Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')
    # return recent_cars
    return  Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')

def delete_last_car():
    Car.objects.last().delete()

# delete_last_car()
# apply_discount()
# print(get_recent_cars())



def task_import(title, description, due_date, is_finished):
    tsk = Task(title=title, description=description, due_date=due_date, is_finished=is_finished)
    tsk.save()
# task_import("Sample Task", "This is a sample task description", "2023-10-31", False)


#
# def show_unfinished_tasks():
#     tsks = Task.objects.filter(is_finished=True)
#     # result = []
#     # for x in tsks:
#     #     print(x.title, x.due_date)
#     #     result.append(f'{x.title}  needs to be done until {x.due_date}')
#     #
#     # return '\n'.join(result)
#     return '\n'.join((f'{x.title} needs to be done until {x.due_date}' for x in tsks))
#     # return "\n".join(str(t) for t in unfinished_tasks)

def show_unfinished_tasks() -> str:
    unfinished_tasks = Task.objects.filter(is_finished=False)

    return "\n".join(str(t) for t in unfinished_tasks)

def complete_odd_tasks():
    all = Task.objects.all()
    for task in all:
        if task.id % 2 == 1:
            task.is_finished = True
    Task.objects.bulk_update(all, ['is_finished'])
# complete_odd_tasks()

def encode_and_replace(text: str, task_title: str):
    # decoded = ''.join(chr(ord(x)-3) for x in text)
    # Task.objects.filter(task_title=task_title).update(description=decoded)
    decoded_text = ''.join(chr(ord(symbol) - 3) for symbol in text)
    Task.objects.filter(title=task_title).update(description=decoded_text)


# encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")
# print(Task.objects.get(title='Simple Task').description)


def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    even_deluxe_rooms = [str(r) for r in deluxe_rooms if r.id % 2 == 0]

    return "\n".join(even_deluxe_rooms)

# print(get_deluxe_rooms())

def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by('id')  # id 1, id 2...

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity is not None:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

    HotelRoom.objects.bulk_update(rooms, ['capacity'])


def reserve_first_room() -> None:
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()
# reserve_first_room()

def delete_last_room() -> None:
    room = HotelRoom.objects.last()

    if not room.is_reserved:
        room.delete()

# print(get_deluxe_rooms())
# reserve_first_room()
# print(HotelRoom.objects.get(room_number=401).is_reserved)
