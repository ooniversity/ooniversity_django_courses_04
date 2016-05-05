from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, pk):
    coaches = Coach.objects.filter(id = pk)
    courses_coach = Course.objects.filter(coach = pk)
    courses_assistant = Course.objects.filter(assistant = pk)
    return render(request, 'coaches/detail.html', {'coaches':coaches, 'courses_coach':courses_coach, 'courses_assistant':courses_assistant})


