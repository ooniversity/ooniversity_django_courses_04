from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, coach_id):

    course_coach = Course.objects.filter(coach=coach_id)
    course_assistant = Course.objects.filter(assistant=coach_id)
    coach_details = Coach.objects.get(id=coach_id)

    return render(request, 'coaches/detail.html', {"details": coach_details, 'course_coach': course_coach, 'course_assistant': course_assistant})