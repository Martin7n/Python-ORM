from django.db import models
from django.core import validators
from django.core.validators import MaxLengthValidator, MinLengthValidator, MinValueValidator, MaxValueValidator

from main_app.custom_manager import AuthorManager


# Create your models here.
#
# class ArticleChoises(models.TextChoices):
#     TECHNOLOGY = "Technology", "Technology"
#     SCIENCE = "Science", "Science"
#     EDUCATION = "Education", "Education"

class Author(models.Model):
    full_name = models.CharField(max_length=100, validators=[validators.MinLengthValidator(3), validators.MaxLengthValidator(100)])
    email = models.EmailField(unique=True)
    is_banned = models.BooleanField(default=False)
    birth_year = models.PositiveIntegerField(validators=[validators.MinValueValidator(1900), validators.MaxValueValidator(2005)])
    website = models.URLField(blank=True, null=True)

    objects = AuthorManager()
    def __str__(self):
        return self.full_name

# class ContentPublishedMixin(models.Model):
#
#     content = models.TextField(validators=[MinLengthValidator(10)])
#     published_on = models.DateTimeField(auto_now_add=True, editable=False)
#
#     class Meta:
#         abstract = True

class Article(models.Model):

    CATEGORIES = (
        ('Technology', 'Technology'),
        ('Science', 'Science'),
        ('Education', 'Education')
    )
    title = models.CharField(max_length=200, validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(200)])
    content = models.TextField(validators=[validators.MinLengthValidator(10)])
    category = models.CharField(max_length=10, choices=CATEGORIES, default="Technology", validators=[validators.MaxLengthValidator(10)])
    authors = models.ManyToManyField(Author, related_name="articles")
    published_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    content = models.TextField(validators=[validators.MinLengthValidator(10)])
    rating = models.FloatField(validators=[validators.MinValueValidator(1.0), validators.MaxValueValidator(5.0)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="reviews")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="reviews")
    published_on = models.DateTimeField(auto_now_add=True, editable=False)
