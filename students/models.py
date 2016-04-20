from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=150)
    skype = models.CharField(max_length=32)
    courses =models.ManyToManyField(Course)

    def __unicode__(self):
        return u'{} {}'.format(self.name, self.surname)
