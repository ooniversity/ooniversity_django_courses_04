from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from django.views.generic.detail import DetailView
from courses.forms import CourseModelForm, LessonModelForm


class CourseDetailView(DetailView):
    model = Course


def detail(request, course_id):
    course_info = get_object_or_404(Course, id=int(course_id))
    lesson_list = Lesson.objects.filter(course_id=course_id)
    
    return render(request, 'courses/detail.html', {'lessons':lesson_list, 'course': course_info})
 
def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            message =  u"Course %s has been successfully added." % application.name
            messages.success(request, message)
            return redirect('/')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form':form})
 
def edit(request, course_id):
    course = get_object_or_404(Course, id = course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance = course)
        if form.is_valid():
            course_form = form.save()
            messages.success(request, u"The changes have been saved.")
            return redirect('courses:edit', course_form.id)
    else:
        form = CourseModelForm(instance = course)
    return render(request, 'courses/edit.html', {'form':form})
 
def remove(request, course_id):
    course = get_object_or_404(Course, id = course_id)
    if request.method == "POST":
        message =  u"Course %s has been deleted." % course.name
        course.delete()
        messages.success(request, message)
        return redirect('/')
    else:
        return render(request, 'courses/remove.html', {'course':course})
 
def add_lesson(request, course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            message =  u"Lesson %s has been successfully added." % lesson.subject
            messages.success(request, message)
            return redirect("courses:detail", lesson.course.id)
    else:
        form = LessonModelForm(initial = {'course':course_id})
    return render(request, 'courses/add_lesson.html', {'form':form})