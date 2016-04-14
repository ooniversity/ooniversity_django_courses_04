from django.contrib.auth.models import User
from django.db import models

class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField(blank=True, null=True)
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=25, blank=True)
    address = models.CharField(max_length=150, blank=True)
    skype = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.get_username()

    def get_name(self):
        return self.user.get_short_name()
    get_name.short_description = 'Name'

    def get_surname(self):
        return self.user.last_name
    get_surname.short_description = 'Surname'
