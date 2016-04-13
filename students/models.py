# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(verbose_name='Nane',max_length=50)
    surname = models.CharField(verbose_name='Surname',max_length=50)
    date_of_birth = models.DateField(verbose_name='Date of birth')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Phone',max_length=20)
    address = models.CharField(verbose_name='Address', max_length=100)
    skype = models.CharField(verbose_name='Skype',max_length=50)
    courses = models.ManyToManyField(Course,verbose_name='Courses')

    def __unicode__(self):
        return  " ".join((self.name, self.surname,)) 

