#coding: utf-8 
from django import forms
from courses.models import Course, Lesson


class CourseModelForm(forms.ModelForm):
    """ Создание формы на основании модели курса """
    class Meta:
        model = Course


class LessonModelForm(forms.ModelForm):
    """ Создание формы на основании модели Lesson """
    class Meta:
        model = Lesson

