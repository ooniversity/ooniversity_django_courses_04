# -*- coding: utf-8 -*-
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
import logging
from students.models import Student

logger = logging.getLogger(__name__)

class StudentListView(ListView):
    model = Student
    paginate_by = 2


    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses__id=course_id)
        else:
            students = Student.objects.all()
        return students


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        logger.debug('Students detail view has been debugged')
        logger.info('Logger of students detail view informs you!')
        logger.warning('Logger of students detail view warns you!')
        logger.error('Students detail view went wrong!')
        return context


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        app = form.save()
        messages.success(self.request, "Student %s has been successfully added." % app.full_name())
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request,"Info on the student has been sucessfully changed.")
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def form_valid(self, form):
        app = Student.objects.get(self.pk)
        messages.success(self.request, "Info on %s has been sucessfully deleted." % app.full_name())
        app = app.delete()
        return super(StudentDeleteView, self).form_valid(form)