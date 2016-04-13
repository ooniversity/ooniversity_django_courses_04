# encoding: utf-8
from django.shortcuts import render
from courses.models import Course
from students.models import Student


def index(request):
    course_qs = Course.objects.all()
    return render(request, 'index.html',
            {"courses":course_qs})

def contact(request):
    return render(request, 'contact.html')

def student_detail(request):
    return render(request, 'student_detail.html')

