from django.shortcuts import render

# Create your views here.
from coaches.models import Coach
from courses.models import Course


def detail(request, coach_id):
    return render(request, 'coaches/detail.html', {'coach': Coach.objects.get(id=coach_id), 
						'course_coach': Course.objects.filter(coach=coach_id), 
						'course_assistant': Course.objects.filter(assistant=coach_id)
    })
