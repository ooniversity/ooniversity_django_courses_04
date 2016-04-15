from django.db import models
from coaches.models import Coach


class Course(models.Model):

    """Table which describe course"""

    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    coach = models.ForeignKey(Coach, null=True, blank=True, related_name='coach_courses')
    assistant = models.ForeignKey(Coach, null=True, blank=True, related_name='assistant_courses')

    def __unicode__(self):
        return self.name


class Lesson(models.Model):

    """Table which describe lesson"""

    subject = models.CharField(max_length=150)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.subject
