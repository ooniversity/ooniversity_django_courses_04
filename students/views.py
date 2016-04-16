from django.shortcuts import render
from students.models import Student
from courses.models import Course

def list_view(request):
    course_id = request.GET.get('course_id')
    try:
        course = Course.objects.get(id = int(course_id))
        students_list = Student.objects.filter(courses=course)
    except TypeError:
        students_list = Student.objects.all()
    return render(request, '../templates/students/list.html', {'students_list': students_list})

def detail(request, id):
    student = Student.objects.get(id = int(id))
    return render(request, '../templates/students/detail.html', {'student': student})

    course_id = request.GET.get('course_id')
    course = Course.objects.get(id = int(course_id))
    if course_id:
        students_list = Student.objects.filter(courses=course)
    else:
        students_list = Student.objects.all()
    return render(request, 'students/list.html', {'students_list': students_list})