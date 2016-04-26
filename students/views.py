# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.core.urlresolvers import reverse_lazy
from students.models import Student

class StudentListView(ListView):
  model = Student
  def get_queryset(self):
    qs = super(StudentListView, self).get_queryset()
    course_id = self.request.GET.get('course_id', None)
    if course_id:
      qs = qs.filter(courses__id=course_id)
    return qs

class StudentDetailView(DetailView):
    model = Student

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

def edit(request, pk):
  student = get_object_or_404(Student, pk=pk)
  if request.method == "POST":
    form = StudentModelForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      messages.success(request, 'Info on the student has been sucessfully changed')
      return redirect('students:edit', student.id)
  else:
    form = StudentModelForm(instance=student)
  return render(request, 'students/edit.html', {'form': form})

def remove(request, pk):
  student = get_object_or_404(Student, pk=pk)
  if request.method == "POST":
    student.delete()
    messages.success(request, u'Info on {} {} has been sucessfully deleted'.format(student.name, student.surname))
    return redirect('students:list_view')
  return render(request, 'students/remove.html')