from django.db import models

from coaches.models import Coach


class Course(models.Model):
    name = models.CharField(max_length=64)
    short_description = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    coach = models.ForeignKey(Coach, blank=True, null=True, related_name='coach_courses')
    assistant = models.ForeignKey(Coach, blank=True, null=True, related_name='assistant_courses')

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.subject
