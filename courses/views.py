from django.shortcuts import render
from courses.models import Course, Lesson

def detail(request, id):
    course = Course.objects.get(id=int(id))
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons})