from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
from students.models import Student

def detail(request, id):
    coach = Coach.objects.get(id = int(id))
    coach_courses = Course.objects.filter(coach=coach)
    assistant_courses = Course.objects.filter(assistant=coach)
    return render(request, 'coaches/detail.html', {'coach': coach, 
    											   'coach_courses':  coach_courses,
    											   'assistant_courses': assistant_courses})