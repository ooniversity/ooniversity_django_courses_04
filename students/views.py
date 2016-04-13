from django.shortcuts import render
from students.models import Student
from courses.models import Course


def list_view(request):
    course_id = request.GET.get('course_id')
    if course_id:
        students = Student.objects.filter(courses=course_id).values()
    else:
        students = Student.objects.all().values()

    for student in students:
        student['courses'] = Course.objects.filter(student=int(student['id']))
    return render(request, 'students/list.html', locals())


def detail(request, number_student):
    student = Student.objects.filter(id=number_student).values()
    for s in student:
        s['courses'] = Course.objects.filter(student=int(s['id']))
    return render(request, 'students/detail.html', locals())