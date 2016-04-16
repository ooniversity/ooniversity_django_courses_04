#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(verbose_name = u'имя', max_length = 255)
    surname = models.CharField(verbose_name = u'фамилия', max_length = 255)
    date_of_birth = models.DateField(verbose_name = u'дата рождения') 
    email = models.EmailField()
    phone = models.CharField(verbose_name = u'телефон', max_length = 255)
    address = models.CharField(verbose_name = u'адрес', max_length = 255)
    skype = models.CharField(max_length = 255)
    courses = models.ManyToManyField(Course)