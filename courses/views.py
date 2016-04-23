from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from courses.models import Course, Lesson

def detail(request, course_id):
	course = get_object_or_404(Course, id=int(course_id))
	lessons = Lesson.objects.filter(course_id=course_id)
	
	return render(request, 'courses/detail.html', locals())
	
