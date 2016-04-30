# encoding: utf-8
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.models import Student
from students.forms import StudentModelForm

class StudentDetailView(DetailView):
    model = Student


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses__id=course_id).order_by('id')
        else:
            students = Student.objects.all()
        return students


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView,self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        application = form.save()
        msg = u"Student %s %s has been successfully added." % (
            application.name, application.surname)
        messages.success(self.request, msg)
        return super(StudentCreateView, self).form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('students:edit')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Student info update"
        return context

    def get_success_url(self):
        return reverse_lazy('students:edit', args=(self.object.id,))

    def form_valid(self, form):
        application = form.save()
        messages.success(
            self.request, u"Info on the student has been sucessfully changed.")
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    template_name_suffix = '_delete_form'
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = u"Student info suppression"
        context['notice'] = u"Студент %s %s будет удален" % (
            self.object.name, self.object.surname)
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Info on {} has been sucessfully deleted.'.format(self.get_object()))
        return super(StudentDeleteView, self).delete(self, request, *args, **kwargs)

