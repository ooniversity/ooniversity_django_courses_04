# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.shortcuts import render, redirect

from courses.models import Course, Lesson
from courses.forms import LessonModelForm


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course_detail'
    template_name = 'courses/detail.html'


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, "Course %s has been successfully added." % form.cleaned_data['name'])
        return super(CourseCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context


class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/edit.html'

    def form_valid(self, form):
        messages.success(self.request, "The changes have been saved.")
        self.success_url = reverse('courses:edit', args=(form.instance.id,))
        return super(CourseUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        messages.success(self.request, "Course %s has been deleted." % course.name)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context


def add_lesson(request, course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            new_lesson = form.save()
            new_message = u'Lesson %s has been successfully added.' % new_lesson.subject
            messages.success(request, new_message)
            return redirect('courses:detail', new_lesson.course.id)
    else:
        form = LessonModelForm()
    return render(request, "courses/add_lesson.html", {'form': form})


'''

def detail(request, course_id):
    lesson = Lesson.objects.filter(course_id=course_id)
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/detail.html', {'course': course, 'lesson': lesson})


def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            new_course = form.save()
            new_message = u'Course %s has been successfully added.' % new_course.name
            messages.success(request, new_message)
            return redirect("/")
    else:
        form = CourseModelForm()
    return render(request, "courses/add.html", {'form': form})


def add_lesson(request, course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            new_lesson = form.save()
            new_message = u'Lesson %s has been successfully added.' % new_lesson.subject
            messages.success(request, new_message)
            return redirect('courses:detail', new_lesson.course.id)
    else:
        form = LessonModelForm()
    return render(request, "courses/add_lesson.html", {'form': form})


def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            new_message = form.save()
            messages.success(request, u'The changes have been saved.')
            return redirect('courses:edit', new_message.id)
    else:
        form = CourseModelForm(instance=course)
    return render(request, "courses/edit.html", {'form': form})


def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        course.delete()
        new_massage = u'Course %s has been deleted.' % course.name
        messages.success(request, new_massage)
        return redirect("/")
    return render(request, "courses/remove.html", {'name': course.name})

'''
