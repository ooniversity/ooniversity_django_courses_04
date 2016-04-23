from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length= 1, choices=(('M','Male'),('F', 'Female')))
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=30)
    description = models.TextField()

    def __unicode__(self):
        return self.user.username

    def first_name_field(self):
        return self.user.first_name
    first_name_field.short_description = "Name"

    def last_name_field(self):
        return self.user.last_name
    last_name_field.short_description = "Surname"
