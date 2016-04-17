from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Coach(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=2, choices=(('M', 'Mail'), ('F', 'Femail')))
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)
    description = models.TextField()
    def __unicode__(self):
        return self.skype
