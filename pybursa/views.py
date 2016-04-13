from courses.models import Course
from django.shortcuts import render
from students.models import Student

def index(request):
    return render(request, 'index.html', {'courses': Course.objects.all()})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    context = []
    for student in Student.objects.all():
        context.append({'student': student,
            'student_courses': Course.objects.filter(student=student)})
    return render(request, 'student_list.html',{'context': context})

def student_detail(request):
    return render(request, 'student_detail.html')
