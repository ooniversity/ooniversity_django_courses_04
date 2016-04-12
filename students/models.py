# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(verbose_name='Имя',max_length=50)
    surname = models.CharField(verbose_name='Фамилия',max_length=50)
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(verbose_name='Телефон',max_length=20)
    address = models.CharField(verbose_name='Адрес', max_length=100)
    skype = models.CharField(verbose_name='Skype',max_length=50)
    courses = models.ManyToManyField(Course)
    
    def __unicode__(self):
        return  " ".join((self.name, self.surname,)) 

