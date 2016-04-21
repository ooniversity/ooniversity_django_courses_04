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
