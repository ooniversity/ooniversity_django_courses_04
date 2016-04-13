 # -*- coding: utf-8 -*-
from django.shortcuts import render
from courses.models import Course

def index(request):
	y=[]
	cours_PyBursa = Course.objects.get(id=1)
	cours_DjBursa = Course.objects.get(id=2)
	cours_JsBursa = Course.objects.get(id=3)
	s = Course.objects.all()
	for a in s:
		y.append(a.short_description)
	print y

	short_description_PyBursa = y[0]
	short_description_DjBursa = y[1]
	short_description_JsBursa = y[2]

	return render(request, 'index.html', {'cours_PyBursa':cours_PyBursa, 'cours_DjBursa':cours_DjBursa, 'cours_JsBursa':cours_JsBursa,
											'short_description_PyBursa':short_description_PyBursa, 'short_description_DjBursa':short_description_DjBursa,
											'short_description_JsBursa':short_description_JsBursa})

def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')

def student_detail(request):
	return render(request, 'student_detail.html')