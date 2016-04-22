# encoding: utf-8
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
from forms import StudentModelForm
from django.contrib import messages

from students.models import Student
from courses.models import Course


def detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'students/detail.html',
             {"student":student})

def list_view(request):
    try:
        course_id=int(request.GET['course_id'])
        students_qs = Student.objects.filter(courses__id=course_id).order_by('id')
        if not students_qs:
            raise ObjectDoesNotExist

    except (ObjectDoesNotExist, ValueError, MultiValueDictKeyError):
        students_qs = Student.objects.all()

    return render(request, 'students/list.html',
            {"students":students_qs})

def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            msg = u"Student {} {} has been successfully added.".format(application.name, application.surname)
            messages.success(request, msg)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, student_id):
    app = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=app)
        if form.is_valid():
            form.save()
            messages.success(request, u"Info on the student has been sucessfully changed.")
    else:
        form = StudentModelForm(instance=app)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):
    app = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        app.delete()
        msg = u"Info on {} {} has been sucessfully deleted.".format(app.name,
                                                                    app.surname)
        messages.success(request, msg)
        return redirect('students:list_view')
    notice = u"The student {} {} will be removed".format(app.name,
                                                         app.surname)
    return render(request, 'students/remove.html', {'notice': notice})
