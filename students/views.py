from django.shortcuts import render
from students.models import Student
from courses.models import Course

def student_list(request):
    course_id=request.GET.get('course_id',None)
    if not course_id:
        stud_list=Student.objects.all()
    else:
        stud_list=Student.objects.filter(courses__id=int(course_id))
    course=Course.objects.all()
    return render(request,"students/list.html",{"student_list":stud_list,"courses":course})

def student_detail(request,num):
    stud=Student.objects.filter(pk=int(num))
    course=Course.objects.all()
    return render(request,"students/detail.html",{"student":stud})
