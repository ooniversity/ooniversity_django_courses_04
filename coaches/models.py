# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=50)
    description = models.TextField()


    def __unicode__(self):
        return self.user.get_username()

    def full_name(self):
        return self.user.get_full_name()

    def surname(self):
        return self.user.last_name
    last_name = property(surname)

    def name(self):
        return self.user.first_name
    first_name = property(name)