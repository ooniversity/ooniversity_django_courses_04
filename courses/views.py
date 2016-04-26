# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from courses.models import Course, Lesson


class CourseDetailView(DetailView):
    model = Course


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        app = form.save()
        messages.success(self.request, "Course %s has been successfully added." % app.name)
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request,"The changes have been saved.")
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def form_valid(self, form):
        app = Course.objects.get(self.pk)
        messages.success(self.request, "Info on %s has been sucessfully deleted." % app.full_name())
        app = app.delete()
        return super(CourseDeleteView, self).form_valid(form)


class LessonCreateView(CreateView):
    model = Lesson
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        context['title'] = "Lesson creation"
        return context

    def form_valid(self, form):
        app = form.save()
        messages.success(self.request, "Lesson %s has been successfully added" % app.subject)
        return super(LessonCreateView, self).form_valid(form)