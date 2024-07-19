from django.db import models
from django.db.models import Q, Sum, Count, QuerySet, Avg, Max, Min
from psycopg2._psycopg import Decimal


class RealEstateListingManager(models.Manager):
    def by_property_type(self,property_type: str):
        return self.filter(property_type=property_type)


    def in_price_range(self, min_price: Decimal, max_price: Decimal):
        query = Q(price__gte=min_price) & Q(price__lte=max_price)
        return self.filter(query)

    def with_bedrooms(self, bedrooms_count: int):
        rooms = self.annotate(room_count=Sum('bedrooms')).filter(room_count=bedrooms_count)
        return rooms

    # def popular_locations(self):
    #     most_locations = self.values('location').annotate(visited=Count("location")).order_by('-visited')
    #     return most_locations

    def popular_locations(self) -> QuerySet:
        return self.values('location').annotate(
            location_count=Count('location')
        ).order_by('-location_count', 'location')[:2]


class VideoGameManager(models.Manager):


    def games_by_genre(self, genre: str):
        return self.filter(genre=genre)

    def recently_released_games(self, year: int):
        return self.filter(release_year__gte=year)

    def highest_rated_game(self):
        #1 return self.order_by('-rating').first()
        #2
        # max_r = self.aggregate(max_rating=max('rating')).order_by('-max_rating').first()['max_rating']
        # game = self.filter(rating=max_r)

        return  self.annotate(max_rating=Max('rating')).order_by('-max_rating').first()

    def lowest_rated_game(self):
        return  self.annotate(min_rating=Min('rating')).order_by('min_rating').first()


    def average_rating(self):
        return f"{self.aggregate(avg_rating=Avg('rating'))['avg_rating']:.1f}"
