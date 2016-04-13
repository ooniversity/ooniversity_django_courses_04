# encoding: utf-8
from django.shortcuts import render
from courses.models import Course, Lesson


def detail(request,id):
    course = Course.objects.get(id=id)
    lessons = Lesson.objects.filter(course=course).order_by('order')
    # l_description =
    return render(request, 'courses/detail.html',
             {"course":course,
              "lessons":lessons,})
              #"l_description":})

# полное описание курса, его название,
#  а также план занятий - название уроков, их порядковые номера и их описание).

    # subject = models.CharField(max_length=200)
    # description = models.TextField()
    # course = models.ForeignKey(Course)
    # order = models.PositiveIntegerField()
