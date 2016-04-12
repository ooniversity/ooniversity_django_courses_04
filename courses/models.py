# encoding: utf-8
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    name = models.CharField(verbose_name='Название',max_length=200)
    short_description = models.CharField(verbose_name='Краткое описание',max_length=1000)
    description = models.TextField(verbose_name='Полное описание')

    def __unicode__(self):
        return  self.name

class Lesson(models.Model):
    subject = models.CharField(verbose_name='Тема',max_length=200)
    description = models.TextField(verbose_name='Описание')
    course = models.ForeignKey(Course,verbose_name='Курс')
    order = models.PositiveIntegerField(verbose_name='Номер по порядку')
    
    def __unicode__(self):
        return  self.subject





