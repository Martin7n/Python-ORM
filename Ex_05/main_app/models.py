from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=40)

class Book(models.Model):
    title = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)



class Song(models.Model):
    title = models.CharField(max_length=100, unique=True)

class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    songs = models.ManyToManyField(Song,  related_name="artists")



class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Review(models.Model):
    description = models.TextField(max_length=200)
    rating = models.PositiveSmallIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")


class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class DrivingLicense(models.Model):
    license_number = models.CharField(max_length= 10)
    issue_date = models.DateField()
    driver = models.OneToOneField(Driver, related_name='license', on_delete=models.CASCADE)

class Owner(models.Model):
    name = models.CharField(max_length=50)

class Car(models.Model):
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    owner = models.ForeignKey(Owner, related_name='cars', blank=True, null=True, on_delete=models.CASCADE)

class Registration(models.Model):
    registration_number = models.CharField(max_length=10, unique=True)
    registration_date = models.DateField(blank=True, null=True)
    car = models.OneToOneField(Car, related_name="registration", blank=True, null=True, on_delete=models.CASCADE)


