# -*- coding: utf-8 -*-
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from students.models import Student


class StudentListView(ListView):
    """
    Output list of the students
    """
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'stud'

    def get_queryset(self):
        try:
            a = self.request.GET['course_id']
            stud_at_course = Student.objects.filter(courses__id=a)
        except MultiValueDictKeyError:
            stud_at_course = Student.objects.all()
        return stud_at_course


class StudentDetailView(DetailView):
    """
    Class for output info about student
    """
    model = Student
    template_name = 'students/detail.html'


class StudentCreateView(CreateView):
    """
    For add students
    """
    model = Student
    template_name = 'students/add.html'
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
    template_name = 'students/edit.html'
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
    template_name = 'students/remove.html'
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = u"Student info suppression"
        return context

    def delete(self, request, *args, **kwargs):
        msg = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, u'Студент %s был удален.' % self.object.full_name)
        return msg
