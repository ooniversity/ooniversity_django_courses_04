# -*- coding: utf-8 -*-
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from courses.models import Course, Lesson


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"

    def get_context_data(self,**kwargs):
        context = super(CourseDetailView,self).get_context_data(**kwargs)
        context["title"] = "Course detail"
        pk = self.kwargs['pk']
        context["lessons"] = Lesson.objects.filter(course_id = pk)
        return context


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = "courses/add.html"

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        app = form.save()
        messages.success(self.request, u"Course %s has been successfully added." % (app.name))
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = "courses/edit.html"

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        context["pk"] = self.kwargs['pk']
        return context

    def form_valid(self,form):
        form.save()
        messages.success(self.request, u'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        self.success_url = reverse('courses:edit', kwargs={'pk': pk})
        return self.success_url


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = "courses/remove.html"

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def form_valid(self, form):
        app = Course.objects.get(self.pk)
        messages.success(self.request, u"Info on %s has been sucessfully deleted." % app.full_name())
        app = app.delete()
        return super(CourseDeleteView, self).form_valid(form)


class LessonCreateView(CreateView):
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        context['title'] = "Lesson creation"
        context["pk"] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        app = form.save()
        messages.success(self.request, u"Lesson %s has been successfully added" % app.subject)
        return super(LessonCreateView, self).form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        self.success_url = reverse('courses:edit', kwargs={'pk': pk})
        return self.success_url