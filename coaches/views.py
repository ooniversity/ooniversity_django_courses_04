from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, pk):
    coach = Coach.objects.get(id=pk)
    coach_trainer = Course.objects.filter(coach=pk)
    coach_assistant = Course.objects.filter(assistant=pk)
    together = {'coach_detail': coach, 'coach_trainer': coach_trainer, 'coach_assistant': coach_assistant}
    return render(request, 'coaches/detail.html', together)
