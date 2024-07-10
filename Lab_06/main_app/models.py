from datetime import datetime, date

from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.



class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)

    @property
    def age(self):
        current_date = date.today()
        return current_date.year - self.birth_date.year - (
                    (current_date.month, current_date.day) < (self.birth_date.month, self.birth_date.day))


class Mammal(Animal):
    fur_color = models.CharField(max_length=50)

class Bird(Animal):
    wing_span = models.DecimalField(max_digits=5, decimal_places=2)
    # def __str__(self):
    #     return f"{self.name}, {self.species}, {self.birth_date}, {self.wing_span}"
class Reptile(Animal):
    scale_type = models.CharField(max_length=50)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number  = models.CharField(max_length=10)

    class Meta:
        abstract = True
class ZooKeeper(Employee):
    SPECIALTY_CHOICES = (
        ("Mammals", "Mammals"),
        ("Birds", "Birds"),
        ("Reptiles", "Reptiles"),
        ("Others", "Others")
    )

    specialty = models.CharField(max_length=10, choices=SPECIALTY_CHOICES)
    managed_animals = models.ManyToManyField(Animal)

    def clean(self):
        if (self.specialty, self.specialty) not in ZooKeeper.SPECIALTY_CHOICES:
            raise ValidationError("Specialty must be a valid choice.")




class Veterinarian(Employee):
    license_number = models.CharField(max_length=10)


class ZooDisplayAnimal(Animal):

    def display_info(self):
        info = ''
        return f"Meet {self.name}! Species: {self.species}, born {self.birth_date}. It makes a noise like '{self.sound}'."

    def is_endangered(self):
        indangered = ["Cross River Gorilla", "Orangutan",  "Green Turtle"]
        if self.species in indangered:
            return f"{self.species} is at risk!"
        else:
            return f"{self.species} is not at risk."

    class Meta:
        proxy = True



