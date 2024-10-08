from django.db import models
from django.db.models import QuerySet, F, Q
from main_app import validators
from main_app.managers import RealEstateListingManager, VideoGameManager
from datetime import timedelta


# Create your models here.


class RealEstateListing(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('House', 'House'),
        ('Flat', 'Flat'),
        ('Villa', 'Villa'),
        ('Cottage', 'Cottage'),
        ('Studio', 'Studio'),
    ]

    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    location = models.CharField(max_length=100)

    objects = RealEstateListingManager()


class VideoGame(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('RPG', 'RPG'),
        ('Adventure', 'Adventure'),
        ('Sports', 'Sports'),
        ('Strategy', 'Strategy'),
    ]

    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    release_year = models.PositiveIntegerField(validators=[validators.RangeValidators(1990, 2023, message="The release year must be between 1990 and 2023")])
    rating = models.DecimalField(max_digits=2,decimal_places=1, validators=[validators.RangeValidators(0.0, 10.0, message="The rating must be between 0.0 and 10.0")])

    def __str__(self):
        return self.title

    objects = VideoGameManager()


class BillingInfo(models.Model):
    address = models.CharField(max_length=200)


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    billing_info = models.OneToOneField(BillingInfo, on_delete=models.CASCADE)

    @classmethod
    def get_invoices_with_prefix(cls, prefix: str):
        # res = []
        # invoices = cls.objects.filter(invoice_number__contains=prefix)
        # for inv in invoices:
        #     res.append(f"Invoice Number with prefix {prefix}: {inv.invoice_number}")
        # return '\n'.join(res)
        return cls.objects.filter(invoice_number__contains=prefix)
        # return cls.objects.filter(invoice_number__startswith=prefix)

    @classmethod
    def get_invoices_sorted_by_number(cls):
        return cls.objects.order_by('invoice_number')

    @classmethod
    def get_invoice_with_billing_info(cls, invoice_number: str):
        return cls.objects.select_related('billing_info').get(invoice_number=invoice_number)


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()




class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.ManyToManyField(Technology, related_name='projects')


    def get_programmers_with_technologies(self):
        return self.programmers.prefetch_related('projects__technologies_used')

class Programmer(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project, related_name='programmers')

    def get_projects_with_technologies(self):
        return self.projects.prefetch_related('technologies_used')

class Task(models.Model):
    PRIORITIES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITIES)
    is_completed = models.BooleanField(default=False)
    creation_date = models.DateField()
    completion_date = models.DateField()

    @classmethod
    def ongoing_high_priority_tasks(cls):

        return cls.objects.filter(priority="High", is_completed=False, completion_date__gte=F('creation_date'))


    @classmethod
    def completed_mid_priority_tasks(cls):
        return cls.objects.filter(priority="Medium", is_completed=True)

    @classmethod
    def search_tasks(cls, query: str):
        return cls.objects.filter(Q(title__contains=query) | Q(description__contains=query))

    @classmethod
    def recent_completed_tasks(cls, days: int):
        return cls.objects.filter(
            is_completed=True,
            completion_date__gte=F('creation_date') - timedelta(days=days))
    #Have a completion date greater than or equal to the creation date subtracted by the given days.....meh

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    difficulty_level = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()

    @classmethod
    def get_long_and_hard_exercises(cls):
        query = Q(duration_minutes__gt=30) & Q(difficulty_level__gte=10)
        return cls.objects.filter(query)

    @classmethod
    def get_short_and_easy_exercises(cls):
        query = Q(duration_minutes__lt=15) & Q(difficulty_level__lt=5)
        return cls.objects.filter(query)

    @classmethod
    def get_exercises_with_difficulty_and_repetitions(cls, min_difficulty: int, min_repetitions: int):
        query = Q(repetitions__gte=min_repetitions) & Q(difficulty_level__gte=min_difficulty)
        return cls.objects.filter(query)

    @classmethod
    def get_exercises_within_duration(cls, min_duration: int, max_duration: int):
        query = Q(duration_minutes__gte=min_duration) & Q(duration_minutes__lte=max_duration)
        return cls.objects.filter(query)
