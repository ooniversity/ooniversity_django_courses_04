# -*- coding: UTF-8 -*-
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from courses.models import Course
from forms import LessonModelForm


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        val = super(CourseCreateView, self).form_valid(form)
        messages.success(self.request, 'Course {} has been successfully added.'.format(self.object.name))
        return val
    
    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context.update({
            "title": 'Course creation'
        })
        return context


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    success_url = '/courses/edit/%(id)d/'

    def form_valid(self, form):
        messages.success(self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context.update({
            "title": 'Course update'
        })
        return context

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        delete = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, 'Course {} has been deleted.'.format(self.object.name))
        return delete

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context.update({
            "title": 'Course deletion'
        })
        return context

def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            message = 'Lesson {} has been successfully added.'.format(lesson.subject)
            messages.success(request, message)
            return redirect('courses:detail', course_id)
    else:
        form = LessonModelForm(initial={'course': course_id})
        return render(request, 'courses/add_lesson.html', {'form':form})
