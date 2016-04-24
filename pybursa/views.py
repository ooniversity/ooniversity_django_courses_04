from django.shortcuts import render
from courses.models import Course, Lesson	


def index(request):
	courses = Course.objects.all()
	return render(request, '../templates/index.html', {'courses':courses})

def contact(request):
    return render(request, '../templates/contact.html', )

def student_list(request):
    return render(request, '../templates/student_list.html', )

def student_detail(request):
    return render(request, '../templates/student_detail.html', )            