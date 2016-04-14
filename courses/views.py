 # -*- coding: utf-8 -*-
from django.shortcuts import render
from courses.models import Course, Lesson



def detail(request, course_id):
	descript = Course.objects.get(id=course_id)
	name = descript.name
	descript = descript.description
	les = Lesson.objects.filter(course = course_id)
	

	return render(request, 'courses/detail.html', {'descript':descript, 'name':name, 'les':les})
