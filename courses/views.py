from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course_id=course_id)
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons})

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid:
            item = form.save()
            messages.success(request, "Course %s has been successfully added." % item.name)
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, "courses/add.html", {'form': form})


def edit(request, course_id):
    item = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            messages.success(request, "The changes have been saved.")
        return redirect('courses:edit', course_id)
    else:
        form = CourseModelForm(instance=item)
    return render(request, "courses/edit.html", {'form': form})

def remove(request, course_id):
    item = Course.objects.get(id=course_id)
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Course %s has been deleted." % item.name)
        return redirect('index')
    return render(request, "courses/remove.html", {'item': item})


def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid:
            item = form.save()
            messages.success(request, "Lesson %s has been successfully added" % item.subject)
            return redirect("courses:detail", course_id)
    else:
        form = LessonModelForm(initial={'news_subscribe':True, 'course': course_id})
    return render(request, "courses/add_lesson.html", {'form': form})


