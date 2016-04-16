<<<<<<< HEAD

=======
>>>>>>> f114d78577c0d563bac959a439787d0446e06ff9
import datetime

from django.db import models
from django.utils import timezone

<<<<<<< HEAD
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):              
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'  
=======

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

>>>>>>> f114d78577c0d563bac959a439787d0446e06ff9

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
<<<<<<< HEAD
    def __unicode__(self):             
        return self.choice_text
      
=======

    def __unicode__(self):
        return self.choice_text

>>>>>>> f114d78577c0d563bac959a439787d0446e06ff9
