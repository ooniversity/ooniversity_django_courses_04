# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from courses.forms import CourseModelForm
from courses.forms import LessonModelForm
from courses.models import Course
from courses.models import Lesson

import logging
logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    logger.debug("Courses detail view has been debugged")
    logger.info("Logger of courses detail view informs you!")
    logger.warning("Logger of courses detail view warns you!")
    logger.error("Courses detail view went wrong!")

    def get_context_data(self, **kwargs):
        course_id = self.kwargs['pk']
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course_id=course_id).order_by('order')
        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

    def form_valid(self, form):
        messages.set_level(self.request, messages.SUCCESS)
        messages.success(self.request, u'Course {0} has been successfully added.'.format(form.cleaned_data.get('name')))
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'students/edit.html'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Course update'
        context['pk'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        messages.set_level(self.request, messages.SUCCESS)
        messages.success(self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('courses:edit', kwargs={'pk': pk})


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        messages.set_level(self.request, messages.WARNING)
        messages.warning(self.request, u'Are you sure you want to delete "{0}"?'.format(kwargs['object'].name))
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context

    def delete(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])
        messages.set_level(request, messages.SUCCESS)
        messages.success(request, u'Course {0} has been deleted.'.format(course.name))
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)


class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        lesson = Lesson()
        lesson.course = get_object_or_404(Course, pk=pk)
        lesson.order = Lesson.objects.filter(course=lesson.course).count() + 1
        kwargs['form'] = LessonModelForm(instance=lesson)
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        context['title'] = u'Создание нового занятия'
        return context

    def form_valid(self, form):
        messages.set_level(self.request, messages.SUCCESS)
        messages.success(self.request, u'Lesson {0} has been successfully added.'.format(form.cleaned_data.get('subject')))
        return super(LessonCreateView, self).form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('courses:detail', kwargs={'pk': pk})


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('order')
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons})

def add(request):
    form = CourseModelForm()
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, u'Course {0} has been successfully added.'.format(form.cleaned_data.get('name')))
            return redirect('index')
    return render(request, 'courses/add.html', {'form': form})


def edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, 'The changes have been saved.')
            redirect('courses:edit', pk=pk)
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        messages.set_level(request, messages.SUCCESS)
        messages.success(request, u'Course {0} has been deleted.'.format(course.name))
        return redirect('index')
    else:
        messages.set_level(request, messages.WARNING)
        messages.warning(request, u'Are you sure you want to delete {0}'.format(course.name))
    return render(request, 'courses/remove.html')


def add_lesson(request, pk):
    lesson = Lesson()
    lesson.course = get_object_or_404(Course, pk=pk)
    lesson.order = Lesson.objects.filter(course=lesson.course).count() + 1
    form = LessonModelForm(instance=lesson)
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, u'Lesson {0} has been successfully added.'.format(form.cleaned_data.get('subject')))
            return redirect('courses:detail', pk=pk)
    return render(request, 'courses/add_lesson.html', {'form': form, 'title': u'Создание нового занятия'})
