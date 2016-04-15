from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=15)
    skype = models.CharField(max_length=15)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        full_name = '{} {}'.format(self.name, self.surname)
        return full_name

    def fname(self):
        full_name = '{} {}'.format(self.name, self.surname)
        return full_name

    full_name = property(fname)
