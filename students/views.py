from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm

def detail(request, student_id):
    student = get_object_or_404(Student, id=int(student_id))
    student_courses_list = student.courses.all()
    return render(request, 'students/detail.html', {'student':student, 'students_courses':student_courses_list})

def list_view(request):
    if request.GET:
        course_id = int(request.GET['course_id'])
        course = get_object_or_404(Course, id=course_id)
        list_of_students = course.student_set.all()
    else:
        list_of_students = Student.objects.all()
    context = {'students_list': list_of_students}

    return render(request, 'students/list.html', context)

def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            message =  "Student %s %s has been successfully added." % (application.name, application.surname)
            messages.success(request, message)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form':form})

def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        message =  "Info on %s %s has been successfully deleted." % (student.name, student.surname)
        student.delete()
        messages.success(request, message)
        return redirect('students:list_view')
    else:
        return render(request, 'students/remove.html', {'student':student})

def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            application = form.save()
            messages.success(request, "Info on the student has been successfully changed.")
            return redirect('students:list_view')
    else:
        form = StudentModelForm(instance=student)
        return render(request, 'students/edit.html', {'form':form})