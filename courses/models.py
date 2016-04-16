from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=64)
    short_description = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.subject
