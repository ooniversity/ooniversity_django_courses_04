from django.shortcuts import render
from students.models import Student
from django.utils.datastructures import MultiValueDictKeyError

def list_view(request):
    try:
        a = request.GET['course_id']
        stud_at_course = Student.objects.filter(courses__id=a)
    except MultiValueDictKeyError:
        stud_at_course = Student.objects.all()

    return render(request, 'students/list.html', {'stud': stud_at_course})


def detail(request, student_id):
    stud_table = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': stud_table})
