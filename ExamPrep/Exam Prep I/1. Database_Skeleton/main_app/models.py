from django.core import validators
from django.db import models

from main_app.custom_manager import DirectorManager


# Create your models here.


# class GenreMovieChoices(models.TextChoices):
#      ACTION = 'Action', 'Action'
#      COMEDY = 'Comedy', 'Comedy'
#      DRAMA = 'Drama', 'Drama'
#      OTHER = 'Other', 'Other'

class Director(models.Model):
    full_name = models.CharField(max_length=120, validators=[validators.MinLengthValidator(2), validators.MaxLengthValidator(120)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, default='Unknown',validators=[validators.MaxLengthValidator(50)])
    years_of_experience = models.SmallIntegerField(default=0, validators=[validators.MinValueValidator(0)])

    objects = DirectorManager()

    def __str__(self):
        return self.full_name
class Actor(models.Model):
    full_name = models.CharField(max_length=120, validators=[validators.MinLengthValidator(2), validators.MaxLengthValidator(120)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, default='Unknown',validators=[validators.MaxLengthValidator(50)])
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
class Movie(models.Model):
    GENRE_CHOICES = (
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Other', 'Other')
    )
    title = models.CharField(max_length=150, validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(150)])
    release_date = models.DateField()
    storyline = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=6, choices=GENRE_CHOICES, default='Other', validators=[validators.MaxLengthValidator(6)])
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, validators=[validators.MinValueValidator(0.0), validators.MaxValueValidator(10.0)])
    is_classic = models.BooleanField(default=False)
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="movies_director")
    starring_actor = models.ForeignKey(Actor, null=True, on_delete=models.SET_NULL, related_name='movies_staring_actors')
    actors = models.ManyToManyField(Actor, related_name="movies_actor")


    def __str__(self):
        return self.title
