from courses.models import Course
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25, blank=True)
    address = models.CharField(max_length=100, blank=True)
    skype = models.CharField(max_length=50, blank=True)
    courses = models.ManyToManyField(Course, blank=True)

    def __unicode__(self):
        return '{} {}'.format(self.name, self.surname)

    def full_name(self):
        return self.__unicode__()
    full_name.short_description = 'Full name'


