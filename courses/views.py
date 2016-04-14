from django.shortcuts import render
from models import Course, Lesson

def index(request):
    
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})


def detail(request, course_id):

    lesson = Lesson.objects.filter(course__id=course_id)
    course_details = Course.objects.get(id__exact=course_id)

    return render(request, 'courses/detail.html', {'details': course_details, 'lesson': lesson})