from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=250)
    short_description = models.CharField(max_length=250)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=250)
    description = models.TextField()
    course = models.ForeignKey('Course')
    order = models.PositiveIntegerField()   #serial number

    def __unicode__(self):
        return self.subject

