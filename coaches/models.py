# -*- coding:UTF-8 -*-
from django.db import models

class Coaches(models.Model):
	user = OneToOneField(User)
  	date_of_birth = DateField()
  	gender = CharField()
  	phone = models.CharField(max_length=24)
	address = models.CharField(max_length=255)
	skype = models.CharField(max_length=128)
	description = TextField()

	def __unicode__(self):
		return self.name