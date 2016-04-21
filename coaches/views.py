# encoding: utf-8
from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

def detail(request, num):
    """ Информация о преподавателе """
    coach = Coach.objects.get(pk = int(num))
    courses_as_coach = Course.objects.filter(coach__id = int(num))
    courses_as_assistant = Course.objects.filter(assistant__id = int(num))
    return render(request, "coaches/detail.html", {"coach": coach, "as_coach": courses_as_coach, "as_assistant": courses_as_assistant})
