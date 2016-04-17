from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=(('M', 'Male'),('F', 'Female')))
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=20)
    description = models.TextField()

    def __unicode__(self):
        return self.user.username


    def name(self):
        return self.user.first_name
    first_name = property(name)

    def surname(self):
        return self.user.last_name
    last_name = property(surname)