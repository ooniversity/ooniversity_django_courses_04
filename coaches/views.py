from django.shortcuts import get_object_or_404
from django.shortcuts import render

from coaches.models import Coach
from courses.models import Course


def detail(request, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id)
    return render(request, 'coaches/detail.html', {'coach': coach})
