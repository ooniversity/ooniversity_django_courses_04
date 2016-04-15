from django.shortcuts import render
from models import Student


def list_view(request):
    course_id = request.GET.get('course_id')
    if course_id is None:
        students = Student.objects.all()
    else:
        students = Student.objects.filter(courses__id=course_id)

    return render(request, 'students/list.html', {'students': students})


def detail(request, student_id):
    student_details = Student.objects.get(id__exact=student_id)

    return render(request, 'students/detail.html', {'student': student_details})