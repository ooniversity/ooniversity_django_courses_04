from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    coach_trainer = Course.objects.filter(coach=coach_id)
    coach_assistant = Course.objects.filter(assistant=coach_id)
    together = {'coach_detail': coach, 'coach_trainer': coach_trainer, 'coach_assistant': coach_assistant}
    return render(request, 'coaches/detail.html', together)
