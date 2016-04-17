from django.shortcuts import render 
from courses.models import Course, Lesson

def index(request):
    course_dict = dict()
    for one_course in Course.objects.all():
        course_dict[one_course.id] = [one_course.name, one_course.short_description]
    print (course_dict)
    return render(request, 'index.html', {'course':course_dict})


#def index(request):     
#    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')
