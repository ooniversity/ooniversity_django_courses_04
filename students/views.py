# encoding: utf-8
from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from forms import StudentModelForm
from django.contrib import messages
from django.template import RequestContext


def list_view(request):
    """ Просмотр списка всех студентов"""
    course_id = request.GET.get('course_id', None)
    if not course_id:
        stud_list = Student.objects.all()
    else:
        stud_list = Student.objects.filter(courses__id = int(course_id))
    course = Course.objects.all()
    return render(request,"students/list.html",{"student_list": stud_list, "courses": course})

    
def detail(request, num):
    """ Полная информация о студенте, на каких курсах занимается """
    std = Student.objects.get(pk = int(num))
    courses = std.courses.all()
    return render(request,"students/detail.html",{"student": std, "courses": courses})

def create(request):
    """ Создание нового студента """
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            std = form.save()
            messages.success(request, u'Student %s %s has been successfully added.'%(std.name, std.surname))
            return redirect('students:list_view')
                
    else:
        form = StudentModelForm()
    return render(request,"students/add.html",{"form":form})

def edit(request, id):
    """ Редактирование данных существующего студента """
    std_instance = Student.objects.get(pk = id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance = std_instance)
        if form.is_valid():
            std = form.save()
            messages.success(request, u'Info on the student has been sucessfully changed.')
            return redirect('students:list_view')
                
    else:
        form = StudentModelForm(instance = std_instance)
    return render(request,"students/edit.html",{"form": form})

def remove(request, id):
    """ Удаление студента с подтверждением """
    std = Student.objects.get(pk = id)
    if request.method == 'POST':
        messages.success(request, u'Info on %s %s has been sucessfully deleted.'%(std.name, std.surname))
        std.delete()
        return redirect('students:list_view')
    return render(request,"students/remove.html", {"student": std})
