from django.shortcuts import render, get_object_or_404
from students.models import Student

def stud_list_by_course_id(request):
    if request.GET:
        student = Student.objects.filter(courses__id=int(request.GET['course_id']))
    else:
        student = Student.objects.all()
    return render(request, 'students/list.html', {'students': student})

def student_detail_by_id(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})
