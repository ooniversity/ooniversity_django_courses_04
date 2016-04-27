# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from pybursa.utils import detail_view
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from courses.models import Lesson


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        course_id = self.kwargs['pk']
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course_id=course_id).order_by('order')
        return context

class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        super_valid = super(CourseCreateView, self).form_valid(form)
        messages.success(self.request, u'Курс {} успешно создан..'.format(self.object.name))
        return super_valid
    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context.update({ "title": u'Course creation' })
        return context


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    success_url = '/courses/edit/%(id)d/'
    def form_valid(self, form):
        messages.success(self.request, u'Данные изменены.')
        return super(CourseUpdateView, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context.update({ "title": u'Course update' })
        return context


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')
    def delete(self, request, *args, **kwargs):
        delete_super = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, u'Курс {} был удален.'.format(self.object.name))
        return delete_super
    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context.update({ "title": u'Course deletion' })
        return context


def add_lesson(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, u'Занятие {} было создано.'.format(lesson.subject))
            return redirect('courses:detail', lesson.course_id)
    else:
        form = LessonModelForm(initial={'course': course})
    return render(request, 'courses/add_lesson.html', {'form': form})