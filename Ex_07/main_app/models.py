
from decimal import Decimal
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models

from main_app.mixins import RechargeEnergyMixin


# Create your models here.


def valid_name(value):
    for x in value:
        if not x.isalpha() and not x.isspace():
            raise ValidationError(message="Name can only contain letters and spaces")
    return value

def valid_age(value):
    if value < 18:
        raise ValidationError(message="Age must be greater than or equal to 18")
    return value

def ph_number(value):
    if not ((len(value) == 13) and (value[1:]).isdigit() and value.startswith("+359")):
        raise ValidationError(message="Phone number must start with '+359' followed by 9 digits")

    return value





class Customer(models.Model):
    name = models.CharField(max_length=100, validators=[valid_name])
    age = models.IntegerField(validators=[valid_age])
    email = models.EmailField(error_messages={'invalid':"Enter a valid email address"})
    phone_number = models.CharField(max_length=13, validators=[ph_number])
    website_url = models.URLField(error_messages={'invalid':"Enter a valid URL"})


class BaseMedia(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', 'title']


class Book(BaseMedia):
    author = models.CharField(
            max_length=100,
            validators=[validators.MinLengthValidator(
                limit_value=5,
                message=f"Author must be at least 5 characters long"
            )]
        )

    isbn = models.CharField(max_length=20, unique=True, validators=[validators.MinLengthValidator(limit_value=6, message="ISBN must be at least 6 characters long")])

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Book"
        verbose_name_plural = "Models of type - Book"

class Movie(BaseMedia):
    director = models.CharField(max_length=100, validators=[validators.MinLengthValidator(limit_value=8, message="Director must be at least 8 characters long")])

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Movie"
        verbose_name_plural = "Models of type - Movie"
class Music(BaseMedia):
    artist = models.CharField(max_length=100, validators=[
        validators.MinLengthValidator(limit_value=9, message="Artist must be at least 9 characters long")])

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Music"
        verbose_name_plural = "Models of type - Music"


class Product(models.Model):
    name = models.CharField(max_length=100,)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_tax(self):
        return self.price * Decimal(0.08)

    @staticmethod
    def calculate_shipping_cost(weight: Decimal):
        return weight * Decimal(2)

    def format_product_name(self):
        return f"Product: {self.name}"

class DiscountedProduct(Product):
    class Meta:
        proxy = True

    def calculate_price_without_discount(self):
        return self.price*Decimal(1.2)

    def calculate_tax(self):
        return self.price * Decimal(0.05)

    @staticmethod
    def calculate_shipping_cost(weight: Decimal):
        return Decimal(weight) * Decimal(1.5)

    def format_product_name(self) -> str:
        return f"Discounted Product: {self.name}"


class Hero(models.Model, RechargeEnergyMixin):
    name = models.CharField(max_length=100)
    hero_title = models.CharField(max_length=100)
    energy = models.PositiveIntegerField(validators=[validators.MinValueValidator(1)])


class SpiderHero(Hero):
    class Meta:
        proxy = True

    def swing_from_buildings(self):
        if self.energy - 80 >= 0:
            self.energy = max(1, self.energy-80)
            self.save()
            return f"{self.name} as Spider Hero swings from buildings using web shooters"
        return f"{self.name} as Spider Hero is out of web shooter fluid"


class FlashHero(Hero):
    class Meta:
        proxy = True
    def run_at_super_speed(self):
        if self.energy - 65 >= 0:
            self.energy = max(1, self.energy-65)
            self.save()
            return f"{self.name} as Flash Hero runs at lightning speed, saving the day"
        return f"{self.name} as Flash Hero needs to recharge the speed force"









