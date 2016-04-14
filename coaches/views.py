from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

def detail(request, num):
    coach = Coach.objects.get(pk=int(num))
    courses_as_assistant = Course.objects.filter(coach__id=int(num))
    courses_as_coach = Course.objects.filter(assistant__id=int(num))
    #lessons_list=course.lesson.all()
    #lessons_list = Lesson.objects.filter(course_id=int(num))
    return render(request,"coaches/detail.html",{"coach":coach, "as_coach":courses_as_coach, "as_assistant":courses_as_assistant})
