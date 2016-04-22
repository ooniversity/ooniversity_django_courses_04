# -*- coding: utf-8 -*-
from django import forms

from courses.models import Course
from courses.models import Lesson

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
