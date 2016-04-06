# -*- coding: cp1251 -*-
from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    """Question class"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):  # __unicode__ on Python 2
        """self str"""
        return unicode(self.question_text)

    def was_published_recently(self):
        """ boolean was_published_recently"""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    """docstring for Choice class"""
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):              # __unicode__ on Python 2
        """self str"""
        return unicode(self.choice_text)
