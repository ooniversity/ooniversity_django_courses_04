from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	skype = models.CharField(max_length=100)
	courses = models.ManyToManyField(Course)
