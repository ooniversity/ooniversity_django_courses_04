﻿from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from courses.models import Course


def index(request):
    #template = loader.get_template('index.html')
    course=Course.objects.all()
    return render(request, 'index.html', {"courses_list":course})



def contact(request):

    return render(request, 'contact.html')


def student_list(request):

    return render(request, 'student_list.html')


def student_detail(request):

    return render(request, 'student_detail.html')
