#coding: utf-8 
from django import forms
from feedbacks.models import Feedback


class FeedbackForm(forms.ModelForm):
    """ Создание формы на основании Feedback """
    class Meta:
        model = Feedback

