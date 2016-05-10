from django.shortcuts import render, redirect
from courses.models import Lesson, Course
from django.contrib import messages
from forms import LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

import logging
logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/detail.html'

    def get_context_data(self, **kwargs):
        logger.debug("Courses detail view has been debugged")
        logger.info("Logger of courses detail view informs you!")
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lesson'] = Lesson.objects.all().filter(course__id=self.kwargs['pk'])
        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Course creation"
        return context

    def form_valid(self, form):
        course = form.save()
        msg = u"Course {0} has been successfully added.".format(course.name)
        messages.success(self.request, msg)
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Course update"
        return context

    def get_success_url(self):
        return reverse_lazy('courses:edit', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        msg = "The changes have been saved."
        messages.success(self.request, msg)
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = u"Course deletion"
        return context

    def delete(self, request, *args, **kwargs):
        msg = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, u"Course %s has been deleted." % self.object.name)
        return msg


def add_lesson(request, pk):
    if request.method == 'POST':
        add_form = LessonModelForm(request.POST)
        if add_form.is_valid():
            a = add_form.cleaned_data['subject']
            add_form.save()
            msg = "Lesson {0} has been successfully added.".format(a)
            messages.success(request, msg)
            return redirect('courses:detail', course_id=pk)
    else:
        add_form = LessonModelForm(initial={'course': pk})
    return render(request, 'courses/add_lesson.html', {'add_form': add_form})
