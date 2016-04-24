from django.shortcuts import render
from courses.models import Course


def index(request):
    course_dict = dict()
    for one_course in Course.objects.all():
         
        course_dict[one_course.id] = one_course
    return render(request, 'index.html', {'course':course_dict})


def contact(request):
    return render(request, 'contact.html')
