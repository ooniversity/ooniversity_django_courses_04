# encoding: utf-8
from django.db import models

class FeedbackForm(models.Model):
    """docstring for FeedbackForm"""

    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    from_email = models.EmailField(max_length=160)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
