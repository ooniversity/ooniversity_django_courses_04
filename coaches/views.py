from django.shortcuts import render

from coaches.models import Coach
from courses.models import Course


def detail(request, id):
    user = Coach.objects.get(id=id)
    course_teacher = Course.objects.filter(coach=id)
    course_assistant = Course.objects.filter(assistant=id)
    data = {'user': user, 'course_teacher': course_teacher, 'course_assistant': course_assistant}
    return render(request, 'coaches/detail.html', data)

