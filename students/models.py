from django.db import models
from courses.models import Course

class Student(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	address = models.CharField(max_length=200)
	skype = models.CharField(max_length=30)
	courses = models.ManyToManyField(Course)

	def __unicode__(self):
		return self.surname

	def my_property(self):
		return "%s %s" % (self.name, self.surname)

	my_property.short_description = "Full name"
	full_name = property(my_property)

