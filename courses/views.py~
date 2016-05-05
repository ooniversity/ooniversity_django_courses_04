from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

import logging
logger = logging.getLogger('courses')

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):        
        logger.debug('Courses detail view has been debugged')
        logger.info('Logger of courses detail view informs you!')
        logger.warning('Logger of courses detail view warns you!')
        logger.error('Courses detail view went wrong!')
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course_id = self.object.pk)
        return context
    

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/add.html'
    context_object_name = 'course'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title']='Course creation'
        return context

    def form_valid(self, form):
        self.application = form.save()
        messages.success(self.request, u'Course {} has been successfully added.'.format(self.application.name)) 
        return super(CourseCreateView, self).form_valid(form) 


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    context_object_name = 'course'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('courses:edit', args = [self.object.pk,])

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context
        
    def form_valid(self, form):
        form.save()
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
        course = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, u'Course {} has been deleted.'.format(self.object.name))
        return course

   
def add_lesson(request, pk):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lessons = form.save()
            messages.success(request, "Lesson %s has been successfully added." %lessons.subject)
            return redirect('courses:detail', lessons.course_id)
    else:
        form = LessonModelForm(initial={'course':pk})
    return render(request, 'courses/add_lesson.html', {'form':form})
