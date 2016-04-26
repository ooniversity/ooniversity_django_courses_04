# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        full_name = "%s %s" % (self.name, self.surname)
        return full_name

    def get_absolute_url(self):
        return reverse('students:edit', kwargs={'pk': self.pk})
