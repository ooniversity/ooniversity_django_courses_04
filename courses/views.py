from django.shortcuts import render
from courses.models import Course, Lesson

def detail(request, num):
    course = Course.objects.get(pk=int(num))
	#lessons_list=course.lesson.all()
    lessons_list = Lesson.objects.filter(course_id=int(num))
    return render(request,"courses/detail.html",{"course":course,"lessons_list":lessons_list})
