from django.utils.datastructures import MultiValueDictKeyError

from django.shortcuts import get_object_or_404
from django.shortcuts import render

from courses.models import Course
from students.models import Student


def list_view(request):
    course = None
    try:
        course = get_object_or_404(Course, pk=request.GET['course_id'])
        students = Student.objects.filter(courses=course).order_by('id')
    except MultiValueDictKeyError:
        students = Student.objects.all().order_by('id')
    context = []
    for student in students:
        context.append({'student': student,
            'student_courses': Course.objects.filter(student=student)})
    return render(request, 'students/list.html',
            {'context': context, 'course':course})


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail.html', {'student': student,
                  'student_courses': Course.objects.filter(student=student)})
