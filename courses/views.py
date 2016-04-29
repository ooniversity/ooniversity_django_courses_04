# encoding: utf-8
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class CourseDetailView(DetailView):
    model = Course
    def get_context_data(self, **kwargs):
        context = super(CourseDetailView,self).get_context_data(**kwargs)
        # print "---->>", kwargs
        context['lessons'] = Lesson.objects.filter(course = kwargs['object'])
        return context


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView,self).get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

    def form_valid(self, form):
        application = form.save()
        msg = u"Course has been successfully added."
        messages.success(self.request, msg)
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name_suffix = '_update_form'
    #success_url = reverse_lazy('courses:edit')

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Course update"
        return context

    def get_success_url(self):
        return reverse_lazy('courses:edit', args=(self.object.id,))

    def form_valid(self, form):
        application = form.save()
        messages.success(
            self.request, u"Info on the course has been sucessfully changed.")
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    template_name_suffix = '_delete_form'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = u"Course deletion"
        context['notice'] = u"Курс %s будет удален" % (
            self.object.name)
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Info on {} has been sucessfully deleted.'.format(self.get_object()))
        return super(CourseDeleteView, self).delete(self, request, *args, **kwargs)


def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            msg = u"Lesson %s has been successfully added." % (application.subject)
            messages.success(request, msg)
            return redirect('courses:detail', application.course.id)
    else:
        form = LessonModelForm(initial = {'course': course_id})
    return render(request, 'courses/add_lesson.html', {'form': form})
