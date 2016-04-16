from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    GENDER_CHOISES = (
        ('M', 'Male'),
        ('F', 'Fimale'),
        )
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOISES)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=250)
    skype = models.CharField(max_length=250)
    description = models.TextField()

    def __unicode__(self):
        return self.user.username

    def first_name_field(self):
        return self.user.first_name
    first_name_field.short_description = "Name"

    def last_name_field(self):
        return self.user.last_name
    last_name_field.short_description = "Surname"