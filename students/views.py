# -*- coding: utf-8 -*-

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# from django.shortcuts import render, redirect

from students.models import Student
# from students.forms import StudentModelForm


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses=course_id)
        return qs


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        student = self.get_object()
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context['title'] = u"Student %s %s detail" % (student.name, student.surname)
        return context


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        messages.success(self.request, u"Student %s %s has been successfully added."
                         % (form.cleaned_data['name'], form.cleaned_data['surname']))
        return super(StudentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Student registration"
        return context


class StudentUpdateView(UpdateView):
    model = Student

    def form_valid(self, form):
        messages.success(self.request, u"Info on the student has been sucessfully changed.")
        return super(StudentUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Student info update"
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, u"Info on %s %s has been sucessfully deleted."
                         % (student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = u"Student info suppression"
        return context

'''

def student_list_view(request):
    if request.GET.get('course_id') is None:
        student = Student.objects.all()
        return render(request, 'students/student_list.html', {'students': student})
    else:
        student = Student.objects.filter(courses__id=request.GET.get('course_id'))
        return render(request, 'students/student_list.html', {'students': student})


def student_detail_view(request, student_id):
        student = Student.objects.get(id=student_id)
        return render(request, 'students/student_detail.html', {'students': student})


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            new_message = u"Student %s %s has been successfully added." % (new_student.name, new_student.surname)
            messages.success(request, new_message)
            return redirect("students:list_view")
    else:
        form = StudentModelForm()
    return render(request, "students/!_old_add.html", {'form': form})


def edit(request, student_id):
    new_student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=new_student)
        if form.is_valid():
            form.save()
            messages.success(request, u"Info on the student has been sucessfully changed.")
    else:
        form = StudentModelForm(instance=new_student)
    return render(request, "students/student_form.html", {'form': form})


def remove(request, student_id):
    new_student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        new_student.delete()
        new_message = u"Info on %s %s has been sucessfully deleted." % (new_student.name, new_student.surname)
        messages.success(request, new_message)
        return redirect("students:list_view")
    return render(request, "students/student_confirm_delete.html", {'name': new_student.name,
                                                                    'surname': new_student.surname})

'''
