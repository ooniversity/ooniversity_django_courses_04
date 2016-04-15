from django.shortcuts import render
from courses.models import Lesson, Course


def detail(request, course_id):
    cours_table = Course.objects.get(id=course_id)
    lesson = Lesson.objects.all().filter(course__name=cours_table.name)
    return render(request, 'courses/detail.html', {"course_table": cours_table, 'lesson': lesson})


    #lesson = Lesson.objects.all().filter(course__name=cours_table.name)