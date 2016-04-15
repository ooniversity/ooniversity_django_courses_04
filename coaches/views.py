from django.shortcuts import get_object_or_404
from django.shortcuts import render

from coaches.models import Coach
from courses.models import Course


def detail(request, coach_id):
    user = get_object_or_404(Coach, pk=coach_id)
    coach_courses = Course.objects.filter(coach=user).order_by('id')
    assistan_courses = Course.objects.filter(assistant=user).order_by('id')
    return render(request, 'coaches/detail.html', {'coach': user,
                  'coach_courses': coach_courses, 'assistant_courses': assistan_courses})
