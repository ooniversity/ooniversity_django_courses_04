from django.utils.datastructures import MultiValueDictKeyError

from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from courses.models import Course
from students.forms import StudentModelForm
from students.models import Student


def list_view(request):
    course = None
    try:
        course = get_object_or_404(Course, pk=request.GET['course_id'])
        students = Student.objects.filter(courses=course)
    except MultiValueDictKeyError:
        students = Student.objects.all()
    context = []
    for student in students:
        context.append({'student': student})
    return render(request, 'students/list.html',
            {'context': context, 'course':course})


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail.html', {'student': student})


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, 'Student {0} {1} has been successfully added.'.format(form.cleaned_data.get('name'), form.cleaned_data.get('surname')))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})


def edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, 'Info on the student has been sucessfully changed.')
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.set_level(request, messages.SUCCESS)
        messages.success(request, 'Info on {0} {1} has been sucessfully deleted.'.format(student.name, student.surname))
        return redirect('students:list_view')
    else:
        messages.set_level(request, messages.WARNING)
        messages.warning(request, 'Are you sure you want to delete {0} {1}'.format(student.name, student.surname))
    return render(request, 'students/remove.html')
