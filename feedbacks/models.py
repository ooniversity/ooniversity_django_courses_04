# encoding: utf-8
from django.db import models
from django.core.urlresolvers import reverse_lazy


class Feedback(models.Model):
    """ Модель для обратной связи """
    name = models.CharField(verbose_name = 'Имя отправителя', max_length = 200)
    subject = models.CharField(verbose_name = 'Тема', max_length = 200)
    message = models.TextField(verbose_name = 'Сообщение')
    from_email = models.EmailField(verbose_name = 'Email')
    create_date = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return  self.name
        
