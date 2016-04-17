from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)

    date_of_birth = models.DateField()
    gender_choices = [
        ['M', 'Male'],
        ['F', 'Female']
    ]
    gender = models.CharField(choices = gender_choices, max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    skype = models.CharField(max_length=30)
    description = models.TextField()

    def __unicode__(self):
        return self.user.username

    def first_name(self, obj):
         return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name