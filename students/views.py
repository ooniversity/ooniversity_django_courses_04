# encoding: utf-8
from django.shortcuts import render
from students.models import Student
from courses.models import Course
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError

def detail(request, id):
    student = Student.objects.get(id=id)

    return render(request, 'students/detail.html',
             {"student":student})

def list_view(request):
    try:
        course_id=int(request.GET['course_id'])
        students_qs = Student.objects.filter(courses__id=course_id).order_by('id')
        if not students_qs:
            raise ObjectDoesNotExist

    except (ObjectDoesNotExist, ValueError, MultiValueDictKeyError):
        students_qs = Student.objects.all()

    return render(request, 'students/list.html',
            {"students":students_qs})
