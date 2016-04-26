# encoding: utf-8
from __future__ import unicode_literals
from django.db import models
from coaches.models import Coach
from django.core.urlresolvers import reverse

class Course(models.Model):
    """ Модель для курсов """
    name = models.CharField(verbose_name = 'Name', max_length = 200)
    short_description = models.CharField(verbose_name = 'Short description', max_length = 1000)
    description = models.TextField(verbose_name = 'Description')
    coach = models.ForeignKey(Coach, blank = True, null = True, related_name = 'coach_courses' )
    assistant = models.ForeignKey(Coach, blank = True, null = True, related_name = 'assistant_courses')

    def __unicode__(self):
        return  self.name
        
        
class Lesson(models.Model):
    """ Модель для уроков, из которых состоят курсы """
    subject = models.CharField(verbose_name = 'Subject', max_length = 200)
    description = models.TextField(verbose_name = 'Description')
    course = models.ForeignKey(Course, verbose_name = 'Courses')
    order = models.PositiveIntegerField(verbose_name = 'Order')
    
    def __unicode__(self):
        return  self.subject

    def get_absolute_url(self):
        pk = self.kwargs['pk']
        #self.success_url = reverse('courses:detail', kwargs={'pk': pk})
        return reverse('courses:detail', kwargs={'pk': pk})#reverse_lazy("courses:detail", 1)



