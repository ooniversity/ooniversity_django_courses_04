from django.shortcuts import render
from courses.models import Course, Lesson

def detail(request, id_course):
    lesson = Lesson.objects.filter(course_id=id_course)
    course = Course.objects.get(id=id_course)
    return render(request, 'courses/detail.html', {'cur_course': course, 'cur_lesson': lesson})
