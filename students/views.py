# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm


def list_view(request):
    if request.GET:
        course_id = int(request.GET['course_id'])
        course = get_object_or_404(Course, id=course_id)
        students_list = course.student_set.all()
        students_list.order_by('id')
    else:
        students_list = Student.objects.all()
        students_list.order_by('id')

    student_courses = dict()

    for st in students_list:
        student_courses[st.id] = st.courses.all()
        s = {
             'students_list': students_list, 
             'course_list': student_courses
             }
    return render(request, 'students/list.html', s)


def detail(request, student_id):
    student = get_object_or_404(Student, id=int(student_id))
    student_courses_list = student.courses.all()
    s = {
         'student':student, 
         'students_courses':student_courses_list
        }
    return render(request, 'students/detail.html', s)


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            app = form.save()
            messages.success(request, u'Student %s %s has been successfully added.'%(app.name, app.surname))
            #data = form.cleaned_data
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form' : form})


def edit(request, student_id):
    
    student_inst = get_object_or_404(Student, id=student_id)    
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance = student_inst)
        if form.is_valid():
            std = form.save()
            messages.success(request, u'Info on the student has been sucessfully changed.')
            return redirect('students:list_view')                
    else:
        form = StudentModelForm(instance = student_inst)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):

    student_inst = get_object_or_404(Student, id=student_id)    
    if request.method == 'POST':
        messages.success(request, u'Info on %s %s has been sucessfully deleted.'%(student_inst.name, student_inst.surname))
        student_inst.delete()
        return redirect('students:list_view')
    return render(request,'students/remove.html', {'student': student_inst})
