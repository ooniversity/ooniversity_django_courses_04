from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, coaches__id):
    coaches = Coach.objects.filter(id = coaches__id)
    courses_coach = Course.objects.filter(coach = coaches__id)
    courses_assistant = Course.objects.filter(assistant = coaches__id)
    return render(request, 'coaches/detail.html', {'coaches':coaches, 'courses_coach':courses_coach, 'courses_assistant':courses_assistant})


