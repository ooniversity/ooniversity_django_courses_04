# -*- coding: utf-8 -*-
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from students.models import Student

import logging
logger = logging.getLogger(__name__)

class StudentListView(ListView):
    """
    Output list of the students
    """
    model = Student
    paginate_by = 2

    def get_context_data(self, **kwargs):
        logger.debug("Students detail view has been debugged")
        logger.info("Logger of students detail view informs you!")
        logger.warning("Logger of students detail view warns you!")
        logger.error("Students detail view went wrong!")
        context = super(StudentListView, self).get_context_data(**kwargs)
        q = self.request.GET.get('course_id')
        context['input'] = q
        return context

    def get_queryset(self):
        queryset = Student.objects.all()
        if self.request.GET.get('course_id'):
            queryset = Student.objects.filter(courses__id=self.request.GET['course_id'])
        return queryset


class StudentDetailView(DetailView):
    """
    Class for output info about student
    """
    model = Student


class StudentCreateView(CreateView):
    """
    For add students
    """
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Student registration"
        return context

    def form_valid(self, form):
        student = form.save()
        msg = u'Студент {0} был добавлен.'.format(student.full_name)
        messages.success(self.request, msg)
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    """
    For updating information about student
    """
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Student info update"
        return context

    def form_valid(self, form):
        msg = u'Данные изменены.'
        messages.success(self.request, msg)
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    """
    For delete student from DB
    """
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = u"Student info suppression"
        return context

    def delete(self, request, *args, **kwargs):
        msg = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, u'Студент %s был удален.' % self.object.full_name)
        return msg
