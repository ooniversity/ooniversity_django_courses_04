from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm

class StudentListView(ListView):
    model = Student

    def  get_queryset(self):
        if self.request.GET:
            course_id = int(self.request.GET['course_id'])
            course = get_object_or_404(Course, id=course_id)
            list_of_students = course.student_set.all()
        else:
            list_of_students = Student.objects.all()
        return list_of_students

class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context