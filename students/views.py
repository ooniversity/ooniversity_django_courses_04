from django.shortcuts import render, redirect

from students.models import Student

from students.forms import StudentModelForm

from django.contrib import messages


def stud_list_by_course_id(request):
    if request.GET.get('course_id'):
        student = Student.objects.filter(courses__id=int(request.GET['course_id']))
    else:
        student = Student.objects.all()
    return render(request, 'students/list.html', {'students': student})

def student_detail_by_id(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid:
            app = form.save()
            messages.success(request, "Student %s has been successfully added." % app.full_name())
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})


def edit(request, student_id):
    app = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=app)
        if form.is_valid():
            app = form.save()
            messages.success(request, "Info on the student has been sucessfully changed.")
        return redirect('students:edit', student_id)
    else:
        form = StudentModelForm(instance=app)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, student_id):
    app = Student.objects.get(id=student_id)
    print 'Enter remove'
    if request.method == 'POST':
        app.delete()
        messages.success(request, "Info on %s has been sucessfully deleted." % app.full_name())
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'app': app})