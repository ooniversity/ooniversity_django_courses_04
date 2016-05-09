from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import *
from django.contrib import messages
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

import logging
logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.get_object().id)
        logger.debug('Courses detail view has been debugged')
        logger.info('Logger of courses detail view informs you!')
        logger.warning('Logger of courses detail view warns you!')
        logger.error('Courses detail view went wrong!')
        return context

class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    context_object_name = 'course'
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Course %s has been successfully added.' % (
                form.instance.name))
        return super(CourseCreateView, self).form_valid(form)
    
class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    context_object_name = 'course'
    def get_success_url(self, **kwargs):
		return reverse_lazy('courses:edit', args=(self.object.pk,))
    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context
    def form_valid(self, form):
        
        messages.success(self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)
    

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    context_object_name = 'course'
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context
    def delete(self, request, *args, **kwargs):
        cours = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, 'Course %s has been deleted.' % 
                self.object.name)
        return cours
    
    

def add_lesson(request, pk):
    res={}   
    if request.POST:
        form = LessonModelForm(request.POST)
        if form.is_valid():
            form.save()
            lesson = form.cleaned_data
            messages.success(request, 'Lesson %s has been successfully added.' % lesson['subject'])
            return redirect('courses:detail', pk)
    else:
        form = LessonModelForm(initial={ 'course': pk })
    res['form'] = form
    return render(request, 'courses/add_lesson.html', res)
        
