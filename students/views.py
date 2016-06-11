# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Student, Course


def list_view(request):
    course_id = request.GET.get('course_id')
    if course_id:
        students = Student.objects.filter(courses=course_id)
        course = Course.objects.get(id=course_id)
        return render(request, 'students/list.html', {'students': students,
                                                      'course': course})
    else:
        students = Student.objects.all()
        return render(request, 'students/list.html',
                      {'students': students})


def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})
