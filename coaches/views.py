from django.shortcuts import get_object_or_404, render

from coaches.models import Coach

def detail(request, coach_id):
    coach = get_object_or_404(Coach, id=int(coach_id))
    return render(request, 'coaches/detail.html', {'coach': coach})