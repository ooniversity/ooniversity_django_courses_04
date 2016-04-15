 # -*- coding: utf-8 -*-
from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length = 150, verbose_name = u'Имя:')
    surname = models.CharField(max_length = 150, verbose_name = u'Фамилия')
    date_of_birth = models.DateField(verbose_name = u'Дата')
    email = models.EmailField(verbose_name = u'Mail')
    phone = models.CharField(max_length = 15, verbose_name = u'Тел.')
    address = models.CharField(max_length = 250, verbose_name = u'Адрес')
    skype = models.CharField(max_length=60, verbose_name = u'Skype')
    courses = models.ManyToManyField(Course)

    def full_name(self):
        return self.name + ' ' + self.surname
