from django.shortcuts import render
from students.models import Student


def list_view(request):
    if request.GET:
        students = Student.objects.filter(courses__id=int(request.GET['course_id']))
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def detail_view(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})

