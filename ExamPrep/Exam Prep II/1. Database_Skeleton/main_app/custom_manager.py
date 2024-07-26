from django.db import models
from django.db.models import Count


class ProfileManager(models.Manager):
    def get_regular_customers(self):
        return self.annotate(
            count_profiles=Count('orders_profile')
        ).filter(count_profiles__gt=2).order_by('-count_profiles')
