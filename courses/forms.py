from django import forms
from courses.models import Lesson, Course


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
