# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
import logging

logger = logging.getLogger(__name__)

'''
class MixinCourseContext(object):
    def get_context_data(self, **kwargs):
        logger.debug("Courses detail view has been debugged")
        logger.info("Logger of courses detail view informs you!")
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")
        context = super(MixinCourseContext, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context
'''

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        logger.debug("Courses detail view has been debugged")
        logger.info("Logger of courses detail view informs you!")
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")
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
    def form_valid(self, form):
        super_valid = super(CourseDeleteView, self).form_valid(form)
        messages.success(self.request, u'Курс {} успешно delete..'.format(self.object.name))
        return super_valid
#    def delete(self, request, *args, **kwargs):
 #       delete_super = super(StudentDeleteView, self).delete(request, *args, **kwargs)
 #       messages.success(self.request, u'Курс был удален.')
 #       return delete_super
    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
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