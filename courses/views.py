# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import logging
logger = logging.getLogger(__name__) # courses.views


''' begin Class-based views '''

class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"
    context_object_name = "course"
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']        
        context["lessons"] = Lesson.objects.filter(course__id = pk)
        logger.debug('Courses detail view has been debugged')
        logger.info('Logger of courses detail view informs you!')
        logger.warning('Logger of courses detail view warns you!')
        logger.error('Courses detail view went wrong!')
        return context

class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')
    fields = '__all__' # if empty - rise an error "RemovedInDjango18Warning: Calling modelform_factory...'fields' or 'exclude'..." 

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Course creation"
        return context

    def form_valid(self, form):
        course = form.save()
        messages.success(self.request, u'Course %s has been successfully added.' % course.name)
        return super(CourseCreateView, self).form_valid(form)

class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__' # if empty - rise an error "RemovedInDjango18Warning: Calling modelform_factory...'fields' or 'exclude'..." 
    template_name = 'courses/edit.html'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Course update"
        return context

    def get_success_url(self):
        return reverse_lazy('courses:edit', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = "courses/remove.html"
    
    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, pk):
        course = self.get_object()
        msg =  u"Course %s has been deleted." % course.name
        course.delete()
        messages.success(self.request, msg)
        return redirect('index')


''' end Class-based views '''

'''
def detail(request, course_id):
    course_info = get_object_or_404(Course, id=int(course_id))
    lesson_list = Lesson.objects.filter(course_id=course_id)
    lesson_list.order_by('order')
    course_get = '?course_id=%d' % course_info.id
    s = {
         'lessons':lesson_list, 
         'course': course_info, 
         'course_get': course_get
        }
    return render(request, 'courses/detail.html', s)



def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, u'Course %s has been successfully added.' % (application.name))
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form' : form})


def remove(request, course_id):
    course_inst = get_object_or_404(Course, id=course_id)    
    if request.method == 'POST':
        messages.success(request, u'Course %s has been deleted.' % (course_inst.name))
        course_inst.delete()
        return redirect('index')
    return render(request,'courses/remove.html', {'course': course_inst})


def edit(request, course_id):    
    course_inst = get_object_or_404(Course, id=course_id)    
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance = course_inst)
        if form.is_valid():
            form.save()
            messages.success(request, u'The changes have been saved.')
            return redirect('courses:edit', course_id)                
    else:
        form = CourseModelForm(instance = course_inst)
    return render(request, 'courses/edit.html', {'form': form})

'''
def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, u'Lesson %s has been successfully added.' % (lesson.subject))
            return redirect('courses:detail', lesson.course.id)
    else:
        course=Course.objects.get(id=course_id)
        form = LessonModelForm(initial = {'course': course})
    return render(request, 'courses/add_lesson.html', {'form' : form})
