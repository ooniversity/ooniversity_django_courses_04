from django.db import models

class Course(models.Model):

    'Table wich describe course'

    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    def __unicode__(self):
        return self.name

class Lesson(models.Model):

    'Table which describe lesson'

    subject = models.CharField(max_length=150)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()
    def __unicode__(self):
        return self.subject
