 # -*- coding: utf-8 -*-
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length = 150, verbose_name = u'Курс:')
    short_description = models.CharField(max_length = 200, verbose_name = u'Краткое описание')
    description = models.TextField(verbose_name = u'Полное описание:')
    
    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length = 200, verbose_name = u'Предмет урока:')
    description = models.TextField(verbose_name = u'Описание урока')
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField(verbose_name = u'Lesson order')
     
    def __unicode__(self):
        return self.subject