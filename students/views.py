from django.shortcuts import render, redirect
from django.contrib import messages
from students.models import Student
from students.forms import StudentModelForm

def list_view(request):
    course_id = request.GET.get('course_id', None)
    if course_id: 
        students = Student.objects.filter(courses__id= course_id)
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'students':students})

def detail(request, students__id):
    students = Student.objects.filter(id = students__id)   
    return render(request, 'students/detail.html', {'students':students})

def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            #data = form.cleaned_data
            students = form.save()
            messages.success(request, 'Student %s %s has been successfully added.' %(students.name, students.surname))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form':form})


def edit(request, students__id):
    students = Student.objects.get(id = students__id)
    #print students
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=students)
        if form.is_valid():
            students = form.save()
            messages.success(request, 'Info on the student has been successfully changed.' %(students.name, students.surname))
            return redirect('/students/edit/students__id/')
    else:
        form = StudentModelForm(instance=students)
    return render(request, 'students/edit.html', {'form':form})

def remove(request, students__id):
    students = Student.objects.get(id = students__id)
    if request.method == 'POST':
        students.delete()
        messages.success(request, 'Info on %s %s has been successfully deleted.' %(students.name, students.surname)) 
        return redirect('students:list_view')         
    return render(request, 'students/remove.html', {'students':students})


