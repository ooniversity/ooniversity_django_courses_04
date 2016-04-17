from django.shortcuts import render

from coaches.models import Coach
from courses.models import Course


def detail(request, coach_id):
    user = Coach.objects.get(id=coach_id)
    course_teacher = Course.objects.filter(coach=coach_id)
    course_assistant = Course.objects.filter(assistant=coach_id)
    parameters = {
        'user': user,
        'course_teacher': course_teacher,
        'course_assistant': course_assistant
    }
    return render(request, 'coaches/detail.html', parameters)
