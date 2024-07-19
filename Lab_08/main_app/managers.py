from django.db import models

class ProductManager(models.Manager):
    def available_products(self):
        prods = self.filter(is_available=True)
        return prods

    def available_products_in_category(self, category_name: str):
        prods = self.filter(is_available=True, category__name=category_name)
        return prods

