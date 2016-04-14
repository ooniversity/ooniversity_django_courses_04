from django.db import models
from courses.models import Course

class Student(models.Model):
    "Table wich describe information about student"
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    skype = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)
    def __unicode__(self):
        return self.name

    def my_property(self):
        return self.name + ' ' + self.surname
    full_name = property(my_property)

