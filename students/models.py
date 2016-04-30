# -*- coding: utf-8 -*-
from django.db import models
from courses.models import Course
from django.core.urlresolvers import reverse

class Student(models.Model):
	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=24)
	address = models.CharField(max_length=255)
	skype = models.CharField(max_length=128)
	courses = models.ManyToManyField(Course)

	def __unicode__(self):
		return self.surname +' ' + self.name

	def Full_name(self):
		return " ".join([self.name, self.surname])
