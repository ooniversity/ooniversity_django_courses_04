from django.shortcuts import render, redirect
from courses.models import Lesson, Course
from django.contrib import messages
from forms import CourseModelForm, LessonModelForm



def detail(request, course_id):
    cours_table = Course.objects.get(id=course_id)
    lesson = Lesson.objects.all().filter(course__name=cours_table.name)
    return render(request, 'courses/detail.html', {"course_table": cours_table, 'lesson': lesson})


def add(request):
    if request.method == 'POST':
        add_form = CourseModelForm(request.POST)
        if add_form.is_valid():
            a = add_form.cleaned_data['name']
            add_form.save()
            msg = "Course {0} has been successfully added.".format(a)
            messages.success(request, msg)
            return redirect('/')
    else:
        add_form = CourseModelForm()
    return render(request, 'courses/add.html', {'form_add_course': add_form})


def edit(request, pk):
    edit_app = Course.objects.get(id=pk)
    if request.method == 'POST':
        edit_form = CourseModelForm(request.POST, instance=edit_app)
        if edit_form.is_valid():
            edit_form.save()
            msg = "The changes have been saved."
            messages.success(request, msg)
    else:
        edit_form = CourseModelForm(instance=edit_app)
    return render(request, 'courses/edit.html', {'edit_form': edit_form})


def remove(request, pk):
    edit_app = Course.objects.get(id=pk)
    context = {}
    context['name'] = edit_app.name
    if request.method == 'POST':
        edit_app.delete()
        msg = "Course {0} has been deleted.".format(context['name'])
        messages.success(request, msg)
        return redirect('/')
    return render(request, 'courses/remove.html', context)
