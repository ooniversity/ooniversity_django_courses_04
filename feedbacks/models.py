# -*- coding: utf-8 -*-
from django.db import models
import datetime


class Feedback(models.Model):
  name = models.CharField(max_length=100)
  subject = models.CharField(max_length=100)
  message = models.TextField()
  from_email = models.EmailField()
  create_date = models.DateTimeField(auto_now_add=datetime.datetime.now())

  def __unicode__(self):
    return self.from_email