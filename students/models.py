from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    skype = models.CharField(max_length=32, null=True, blank=True)
    courses = models.ManyToManyField(Course)
