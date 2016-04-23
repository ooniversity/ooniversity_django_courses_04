from django.shortcuts import render, redirect
from django.contrib import messages

from students.models import Student
from students.forms import StudentModelForm


# Create your views here.

def student_list_view(request):
    if request.GET.get('course_id') is None:
        student = Student.objects.all()
        return render(request, 'students/list.html', {"students": student})
    else:
        student = Student.objects.filter(courses__id=request.GET.get
                                         ("course_id"))
        return render(request,
                      'students/list.html', {"students": student})


def student_detail_view(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request,
                  'students/detail.html', {"student": student})


def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            message = u"Student %s %s has \
                       been successfully added." \
                        % (application.name, application.surname)
            messages.success(request, message)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})


def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        message = u"Info on %s %s has \
                   been sucessfully deleted." % (student.name, student.surname)
        student.delete()
        messages.success(request, message)
        return redirect("students:list_view")
    else:
        return render(request, 'students/remove.html',
                      {"student": student})


def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, u"Info on the student has \
                                       been sucessfully changed.")
            return render(request, 'students/edit.html', {'form': form})
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {"form": form})
