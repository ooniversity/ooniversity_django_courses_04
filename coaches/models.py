from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=75)
    skype = models.CharField(max_length=50)
    description = models.TextField()

    Male = 'M'
    Female = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),
        )
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              default=Male
                              )

    def __unicode__(self):
        return self.user.username

    def name(self):
        return self.user.first_name
    first_name = property(name)

    def surname(self):
        return self.user.last_name
    last_name = property(surname)

