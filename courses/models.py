from django.db import models
from coaches.models import Coach


class Course(models.Model):
    name = models.CharField(max_length=250)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    coach = models.ForeignKey(Coach, related_name='coach_courses', null=True, blank=True)
    assistant = models.ForeignKey(Coach, null=True, related_name='assistant_courses', blank=True)


    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=250)
    description = models.TextField()
    course = models.ForeignKey('Course')
    order = models.PositiveIntegerField()   #serial number

    def __unicode__(self):
        return self.subject

