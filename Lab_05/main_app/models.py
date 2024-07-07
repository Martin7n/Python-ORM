from datetime import datetime, date

from django.db import models

# Create your models here.


class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def  __str__(self):
        return self.first_name + ' ' + self.last_name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    lecturer = models.ForeignKey(to="Lecturer", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    subjects = models.ManyToManyField(to='Subject',
        through='StudentEnrollment')

class GradeChoice(models.TextChoices):
        A = 'A', 'A'
        B = 'B', 'B'
        C = 'C', 'C'
        D = 'D', 'D'
        F = 'F', 'F'


class StudentEnrollment(models.Model):
    student = models.ForeignKey(to="Student", on_delete=models.CASCADE)
    subject = models.ForeignKey(to="Subject", on_delete=models.CASCADE)

    enrollment_date = models.DateField(default=date.today())

    grade = models.CharField(max_length=1, choices=GradeChoice.choices)
    #
    # def __str__(self):
    #     return f"{student.first_name} {student.last_name} is enrolled in {enrollment.subject}.
    #


class LecturerProfile(models.Model):
    lecturer = models.OneToOneField(to='Lecturer', null=True, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    office_location = models.CharField(max_length=100, blank=True,null=True)



