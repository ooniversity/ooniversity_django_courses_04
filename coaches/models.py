# encoding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    """ Модель для преподавателя """
    user = models.OneToOneField(User)
    date_of_birth = models.DateField(verbose_name = 'Date of birth')
    gender = models.CharField(choices=(('M', 'Male'),('F', 'Female'),), verbose_name = 'Sex', max_length = 1)
    phone = models.CharField(verbose_name = 'Phone', max_length = 20)
    address = models.CharField(verbose_name = 'Address', max_length = 100)
    skype = models.CharField(verbose_name = 'Skype', max_length = 50)
    description = models.TextField(verbose_name = 'Description')

    def __unicode__(self):
        return self.user.username
   
