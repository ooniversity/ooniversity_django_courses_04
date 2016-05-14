from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from django.contrib import messages


from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

import logging
logger = logging.getLogger(__name__)

class CourseDetailView(DetailView):
    model = Course
    logger.debug("Courses detail view has been debugged")
    logger.info("Logger of courses detail view informs you!")
    logger.warning("Logger of courses detail view warns you!")
    logger.error("Courses detail view went wrong!")

class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/add.html'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        application = form.save()
        message =  u"Course %s has been successfully added." % application.name
        messages.success(self.request, message)
        return super(CourseCreateView, self).form_valid(form)    

class CourseUpdateView(UpdateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/edit.html'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def form_valid(self, form):
        application = form.save()
        message =  u"Course %s has been successfully updated." % application.name
        messages.success(self.request, message)
        return super(CourseUpdateView, self).form_valid(form)

def remove(request, course_id):
	course = get_object_or_404(Course, id=course_id)
	if request.method == "POST":
	    message =  u"Course %s has been deleted." % (course.name)
	    course.delete()
	    messages.success(request, message)
	    return redirect('/')
	else:
	    return render(request, 'courses/remove.html', {'course':course})    

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        message =  u"Course %s has been  deleted." % course.name
        messages.success(self.request, message)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)


def add_lesson(request):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            message = u"Lesson %s has been successfully added." % (lesson.subject)
            messages.success(request, message)
            return redirect('courses:detail', lesson.course.id )
    else:
        form = LessonModelForm()    
    return render(request, 'courses/add_lesson.html', {'form':form})       
