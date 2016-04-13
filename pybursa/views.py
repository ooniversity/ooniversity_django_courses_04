# -*- coding: cp1251 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from courses.models import Course


def index(request):
    c = Course.objects.values()
    return render(request, 'index.html', locals())


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')
