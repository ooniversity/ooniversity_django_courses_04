# -*- coding:UTF-8 -*-
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from courses.models import Course

def course_descripts(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses} )

def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')

def student_detail(request):
	return render(request, 'student_detail.html')

def custom_404_server_error(request):
	response = render_to_response('404.html')
	response.status_code = 404
	return response

def custom_500_server_error(request):
	response = render_to_response('500.html')
	response.status_code = 500
	return response 
