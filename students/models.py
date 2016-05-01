from courses.models import Course
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return '{} {}'.format(self.name, self.surname)

    def full_name(self):
        return self.__unicode__()
    full_name.short_description = 'Full name'


