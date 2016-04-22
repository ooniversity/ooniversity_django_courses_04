from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

def detail(request, id):
    course = Course.objects.get(id=id)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons})

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            message = "Course {} has been successfully added."
            messages.success(request, message.format(course.name))
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, "courses/add.html", {"form": form})

def add_lesson(request,id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            message = "Lesson {} has been successfully added."
            messages.success(request, message.format(lesson.subject))
            return redirect('courses:detail', lesson.course.id)
    else:
        form = LessonModelForm(initial={'course': id})
        return render(request, "courses/add_lesson.html", {"form": form})

def edit(request, id):
    course_data = Course.objects.get(id=id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course_data)
        if form.is_valid():
            form.save()
            message = "The changes have been saved."
            messages.success(request, message)
            return redirect("courses:edit", id)
    else:
        form = CourseModelForm(instance=course_data)
    return render(request, "courses/edit.html", {"form": form})
    
def remove(request, id):
    course_data = Course.objects.get(id=id)
    if request.method == 'POST':
        message = "Course {} has been deleted."
        course_data.delete()
        messages.success(request, message.format(course_data.name))
        return redirect('index')
    return render(request, "courses/remove.html", {"course_data": course_data})