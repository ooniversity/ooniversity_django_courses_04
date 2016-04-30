from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses=course_id)
        return qs


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context["title"] = "Student registration"
        context["jambotron_h1"] = "Add new student"
        context["btn_text"] = "Add"
        return context

    def form_valid(self, form):
        student = form.save()
        message =  u"Student %s %s has been successfully added." % (student.name, student.surname)
        messages.success(self.request, message)
        return super(StudentCreateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def delete(self, request, pk):
        student = self.get_object()
        message = u"Info on %s %s has been sucessfully deleted." % \
                  (student.name, student.surname)
        student.delete()
        messages.success(self.request, message)
        return redirect('students:list_view')


class StudentUpdateView(UpdateView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Student info update"
        context["jambotron_h1"] = "Edit student"
        context["btn_text"] = "Update"
        return context

    def form_valid(self, form):
        form.save()
        message = u"Info on the student has been sucessfully changed."
        messages.success(self.request, message)
        return super(StudentUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('students:edit', args=[self.get_object().id])
