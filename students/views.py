from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from django.contrib import messages
from students.forms import StudentModelForm

def list_view(request):
    course_id = request.GET.get('course_id')
    try:
        course = Course.objects.get(id = int(course_id))
        students_list = Student.objects.filter(courses=course)
    except TypeError:
        students_list = Student.objects.all()
    return render(request, 'students/list.html', {'students_list': students_list})

def detail(request, id):
    student = Student.objects.get(id = int(id))
    return render(request, 'students/detail.html', {'student': student})

def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            data = request.POST
            message = "Student {} {} has been successfully added."
            messages.success(request, message.format(data['surname'], data['name']))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, "students/add.html", {"form": form})
    
def edit(request, id):
    student_data = Student.objects.get(id = id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student_data)
        if form.is_valid():
            student_data = form.save()
            message = "Info on the student has been sucessfully changed."
            messages.success(request, message)
            return redirect('students:list_view')
    else:
        form = StudentModelForm(instance=student_data)
    return render(request, "students/edit.html", {"form": form})
    
def remove(request, id):
    student_data = Student.objects.get(id = id)
    if request.method == 'POST':
        message = "Info on {} {} has been sucessfully deleted."
        student_data.delete()
        messages.success(request, message.format(student_data.name, student_data.surname))
        return redirect('students:list_view')
    return render(request, "students/remove.html", {"student_data": student_data})
