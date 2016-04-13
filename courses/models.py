from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.subject
