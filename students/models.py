# -*- coding: utf-8 -*-
import datetime
from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):              # __str__ on Python 3
        return '%s %s' % (self.name, self.surname)
