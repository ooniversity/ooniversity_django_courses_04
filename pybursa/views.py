# -*- coding: utf-8 -*-

from django.shortcuts import render
from courses.models import Course


def old_index(request):
    return render(request, 'old_index.html')


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')


def index(request):
    courses_list = Course.objects.all()
    return render(request, 'index.html', {'courses_list': courses_list})
