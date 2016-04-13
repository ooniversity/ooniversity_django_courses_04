from django.shortcuts import render
from students.models import Student

def list_view(request):
    if request.GET.get('course_id') == None:
        student = Student.objects.all()
        return render(request, 'students/list.html', {'cur_students': student})
    else:
        student = Student.objects.filter(courses__id=request.GET.get('course_id'))
        return render(request, 'students/list.html', {'cur_students': student})

def detail(request, student_id):
        student = Student.objects.get(id=student_id)
        return render(request, 'students/detail.html', {'cur_students': student})
