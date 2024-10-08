from django.core import validators
from django.db import models

from main_app.custom_manager import ProfileManager


# Create your models here.


class Profile(models.Model):
    full_name = models.CharField(max_length=100, validators=[validators.MaxLengthValidator(100), validators.MinLengthValidator(2)])
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, validators=[validators.MaxLengthValidator(15)])
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    objects = ProfileManager()


class Product(models.Model):
    name = models.CharField(max_length=100, validators=[validators.MaxLengthValidator(100)])
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,validators=[validators.MinValueValidator(0.01)])
    in_stock = models.PositiveIntegerField(validators=[validators.MinValueValidator(0)])
    is_available = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders_profile')
    products = models.ManyToManyField(Product, related_name='orders_products')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validators.MinValueValidator(0.01)])
    creation_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)


