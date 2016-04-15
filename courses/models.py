from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.subject
