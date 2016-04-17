from django.db import models

from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    skype = models.CharField(max_length=64)
    description = models.TextField(max_length=256)

    def __unicode__(self):
        return self.user.get_username()

    def user_name(self):
        return self.user.get_full_name()
