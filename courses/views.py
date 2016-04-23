from django.shortcuts import render, redirect
from django.contrib import messages

from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm


def detail(request, course_id):

    lesson = Lesson.objects.filter(course__id=course_id)
    course_details = Course.objects.get(id__exact=course_id)

    return render(request, 'courses/detail.html', {'details': course_details, 'lesson': lesson})

def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course_name = form.cleaned_data["name"]
            form.save()
            messages.success(request, "Course %s has been successfully added." % course_name)
            return redirect('index')
    else:
        form = CourseModelForm()

    return render(request, 'courses/add.html', {"form": form})


def edit(request, course_id):
    update_record = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=update_record)
        if form.is_valid():
            form.save()
            messages.success(request, "The changes have been saved.")
    else:
        form = CourseModelForm(instance=update_record)

    return render(request, 'courses/edit.html', {"form": form})


def remove(request, course_id):
    remove_record = Course.objects.get(id=course_id)
    course_name = remove_record.name
    if request.method == "POST":
        remove_record.delete()
        messages.success(request, "Course %s has been deleted." % course_name)
        return redirect("index")

    return render(request, 'courses/remove.html', {"name": course_name})

def add_lesson(request, course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson_name = form.cleaned_data["subject"]
            form.save()
            messages.success(request, "Lesson %s has been successfully added." % lesson_name)
            return redirect('courses:detail', course_id=course_id)
    else:
        form = LessonModelForm(initial={'course': course_id})

    return render(request, 'courses/add-lesson.html', {"form": form})