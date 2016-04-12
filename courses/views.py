from django.shortcuts import render
from courses.models import Course, Lesson

def course_details(request, num):
    course = Course.objects.get(pk=int(num))
    lessons_list = Lesson.objects.filter(course_id=int(num))
    return render(request,"detail.html",{"course":course,"lessons_list":lessons_list})
