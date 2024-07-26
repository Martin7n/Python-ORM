from django.core.validators import MaxLengthValidator, MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import TennisPlayerManager


# Create your models here.

class SurfaceChoices(models.TextChoices):
    NOT_SELECTED = "Not Selected", "Not Selected"
    CLAY = "Clay","Clay"
    GRASS = "Grass","Grass"
    HARD_COURT= "Hard Court", "Hard Court"
class TennisPlayer(models.Model):
    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(5), MaxLengthValidator(120)])
    #TODO'''validator min5'''
    birth_date = models.DateField()
    country = models.CharField(max_length=100, validators=[MinLengthValidator(2), MaxLengthValidator(100)] )
    #TODO minlen2
    ranking = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(300)])
    #TODO min1 max300''')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    objects = TennisPlayerManager()

class Tournament(models.Model):
    name = models.CharField(max_length=150, unique=True,validators=[MinLengthValidator(2), MaxLengthValidator(150)] )
    #TODO min12 max 150
    location = models.CharField(max_length=100, validators=[MinLengthValidator(2), MaxLengthValidator(100)])
    #TODO min2 max 100
    prize_money = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    surface_type = models.CharField(max_length=12, choices=SurfaceChoices.choices, default="Not Selected", validators=[ MaxLengthValidator(12)])
    ## TODO validation: Maximum length of 12 characters.
    # Valid choices: "Not Selected", "Clay", "Grass", and "Hard Court".
    def __str__(self):
        return self.name
class Match(models.Model):
    score = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    #TODO Validations: Maximum length of 100 characters.
    summary = models.TextField(validators=[MinLengthValidator(5)])
    #TODO Validations: Minimum length of 5 characters.
    date_played = models.DateTimeField()
    tournament =models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches')
    players = models.ManyToManyField(TennisPlayer, related_name="matches")
    winner = models.ForeignKey(TennisPlayer, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='matches_won')
    #TODO Make sure the plural name for the Match model is set correctly to Matches (hint: set it in the Meta class).

    def __str__(self):
        return f"Match in {self.tournament.name} on {self.date_played}"

    class Meta:
        verbose_name_plural = "Matches"

