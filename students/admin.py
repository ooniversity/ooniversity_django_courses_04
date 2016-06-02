from django.contrib import admin
from .models import Student
from courses.models import Course, Lesson

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Lesson)
