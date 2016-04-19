#coding: utf-8 
from django import forms
from students.models import Student

class StudentModelForm(forms.ModelForm):
    """ Создание формы на основании модели студента """
    class Meta:
        model = Student


