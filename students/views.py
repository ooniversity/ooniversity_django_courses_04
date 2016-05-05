# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from students.models import Student
import logging
logger = logging.getLogger(__name__)


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
        logger.debug("Students detail view has been debugged")
        logger.info("Logger of students detail view informs you!")
        logger.warning("Logger of students detail view warns you!")
        logger.error("Students detail view went wrong!")
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        student = self.get_object()
        context['title'] = u"Student detail"
        return context


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        super_valid = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request,
                         u'Студент {} {} успешно добавлен.'.format(self.object.name, self.object.surname))
        return super_valid

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context.update({
            "title": u'Создание нового студента'
        })
        return context


class StudentUpdateView(UpdateView):
    model = Student
    success_url = '/students/edit/%(id)d/'

    def form_valid(self, form):
        messages.success(self.request, u'Данные изменены.')
        return super(StudentUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context.update({
            "title": u'Редактирование данных студента'
        })
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')

    def delete(self, request, *args, **kwargs):
        delete_super = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request,
                         u'Студент {} {} был удален.'.format(self.object.name, self.object.surname))
        return delete_super
