﻿import datetime

from django.db import models
from django.utils import timezone

class Course(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()
    def __unicode__(self):
        return self.subject