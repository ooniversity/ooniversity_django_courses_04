from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages

def list_view(request):
    if request.GET:
        students = Student.objects.filter(courses__id=int(request.GET['course_id']))
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def detail_view(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})

def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid:
            item = form.save()
            messages.success(request, "Student %s has been successfully added." % item.full_name())
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})


def edit(request, student_id):
    item = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            messages.success(request, "Info on the student has been sucessfully changed.")
        return redirect('students:edit', student_id)
    else:
        form = StudentModelForm(instance=item)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):
    item = Student.objects.get(id=student_id)
    print 'Enter remove'
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Info on %s has been sucessfully deleted." % item.full_name())
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'item': item})
