from django.shortcuts import render
from courses.models import Course
from students.models import Student
from coaches.models import Coach

def detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    course_coach = Course.objects.filter(coach=coach_id)
    course_assistant = Course.objects.filter(assistant=coach_id)
    return render(request, 'coaches/detail.html', {'cur_cur_coach': course_coach, 'cur_coach': coach, 'cur_cur_assistant': course_assistant})
    
