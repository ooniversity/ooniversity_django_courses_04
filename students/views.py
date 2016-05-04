# -*- coding: UTF-8 -*-
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from students.models import Student


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs


class StudentDetailView(DetailView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super(StudentDetailView,self).get_context_data(**kwargs)
        logger.debug('Students detail view has been debugged')
        logger.info('Logger of students detail view informs you!')
        logger.warning('Logger of students detail view warns you!')
        logger.error('Students detail view went wrong!')
        context['courses'] = Course.objects.filter(student__id = self.object.id)
        return context


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        val = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request,
                         'Student {} {} has been successfully added.'.format(self.object.name, self.object.surname))
        return val

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context.update({
            "title": 'Student registration'
        })
        return context


class StudentUpdateView(UpdateView):
    model = Student
    success_url = '/students/edit/%(id)d/'

    def form_valid(self, form):
        messages.success(self.request, 'Info on the student has been sucessfully changed.')
        return super(StudentUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context.update({
            "title": 'Student info update'
        })
        return context

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def delete(self, request, *args, **kwargs):
        delete = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, 'Info on {} {} has been sucessfully deleted.'.format(self.object.name, self.object.surname))
        return delete

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context.update({
            "title": 'Student info suppression'
        })    
        return context
