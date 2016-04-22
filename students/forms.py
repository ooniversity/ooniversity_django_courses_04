# encoding: utf-8
from django import forms
from students.models import Student
from django.forms.extras.widgets import SelectDateWidget

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        #help_texts = {'username':'',}
        #fields = ['username', 'password']
        widgets = {
           'date_of_birth': SelectDateWidget(),
        }
