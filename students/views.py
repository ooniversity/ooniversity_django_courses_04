from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from forms import StudentModelForm
from django.contrib import messages
from django.template import RequestContext

def list_view(request):
    course_id=request.GET.get('course_id',None)
    if not course_id:
        stud_list=Student.objects.all()
    else:
        stud_list=Student.objects.filter(courses__id=int(course_id))
    course=Course.objects.all()
    return render(request,"students/list.html",{"student_list":stud_list,"courses":course})

def detail(request,num):
    std=Student.objects.get(pk=int(num))#filter(pk=int(num))
    courses=std.courses.all()#Course.objects.filter(pk__in=std.courses)
    #courses=Course.objects.filter(pk=std__courses__id)
    return render(request,"students/detail.html",{"student":std,"courses":courses})

def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            std= form.save()
            messages.success(request, u'Student %s %s has been successfully added.'%(std.name, std.surname))
            return redirect('students:list_view')
                
    else:
        form = StudentModelForm()
    return render(request,"students/add.html",{"form":form})

def edit(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            std= form.save()
            messages.success(request, u'Student %s %s has been successfully added.'%(std.name, std.surname))
            return redirect('students:list_view')
                
    else:
        form = StudentModelForm()
    return render(request,"students/edit.html",{"form":form})

def remove(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            std= form.save()
            messages.success(request, u'Student %s %s has been successfully added.'%(std.name, std.surname))
            return redirect('students:list_view')
                
    else:
        form = StudentModelForm()
    return render(request,"students/remove.html",{"form":form})
