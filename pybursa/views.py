from django.shortcuts import render
from courses.models import Course
import datetime

def index(request):
	courses = Course.objects.only('name', 'short_description', 'id')
	my_list=['python', 'html', 'javascript']
	return render(request, 'index.html', {"courses": courses,'my_list':my_list})

def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')

def student_detail(request):
	return render(request, 'student_detail.html')
