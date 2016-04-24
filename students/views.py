from django.shortcuts import get_object_or_404, render, redirect
from datetime import date
from students.models import Student
from courses.models import Course
from forms import StudentModelForm
from django.contrib import messages
from django.template import RequestContext

def detail(request, student_id):
    student = get_object_or_404(Student, id=int(student_id))
    student_courses_list = student.courses.all()
    return render(request, 'students/detail.html', {'student':student, 'students_courses':student_courses_list})

def list_view(request):
    if request.GET:
        course_id = int(request.GET['course_id'])
        course = get_object_or_404(Course, id=course_id)
        list_of_students = course.student_set.all()
        list_of_students.order_by('id')
    else:
        list_of_students = Student.objects.all()
        list_of_students.order_by('id')

    student_courses = dict()
    for stud in list_of_students:
        student_courses[stud.id] = stud.courses.all()
    return render(request, 'students/list.html', {'students_list': list_of_students, 'course_list': student_courses})

def create(request):
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
    std = Student.objects.get(pk = id)
    if request.method == 'POST':
        messages.success(request, u'Info on %s %s has been sucessfully deleted.'%(std.name, std.surname))
        std.delete()
        return redirect('students:list_view')
    return render(request,"students/remove.html", {"student": std})