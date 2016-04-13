# encoding: utf-8
from django.shortcuts import render
from students.models import Student


def detail(request, id):
    student = Student.objects.get(id=id)
    #date_of_birth = student.date_of_birth.strftime('%b. %d, %Y')
    # lessons = Lesson.objects.filter(course=course)
    # lessons = students.courses.all()
    return render(request, 'students/detail.html',
             {"student":student})#, "date_of_birth":date_of_birth})

def list_view(request):
    students_qs = Student.objects.all()
    courses_all = 1
    return render(request, 'students/list_view.html',
            {"students":students_qs})
