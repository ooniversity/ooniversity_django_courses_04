 # -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from courses.models import Course

def index(request):
	cours = Course.objects.all()
	return render(request, 'index.html', {'cours':cours})

def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')

def student_detail(request):
	return render(request, 'student_detail.html')

def my_custom_page_not_found_view(request):
	return render_to_response('404.html')

def my_custom_error_view(request):
	return render_to_response('500.html')