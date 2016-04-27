# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from students.forms import StudentModelForm
from students.models import Student
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
 

class StudentListView(ListView):
    model = Student
    
    context_object_name = 'stud'
  
    def get_queryset(self):
        try:
            a = self.request.GET['course_id']
            stud_at_course = Student.objects.filter(courses__id=a)
        except MultiValueDictKeyError:
            stud_at_course = Student.objects.all()
        return stud_at_course
  
 """
def list_view(request):
    course_id = request.GET.get('course_id', None)
    if course_id:
        students = Student.objects.filter(courses__id=course_id)
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})
"""

class StudentDetailView(DetailView):
    model = Student
    
 """
def detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/detail.html', {'student': student})
"""

class StudentCreateView(CreateView):
    model = Student
    
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Student registration"
        return context
  
    def form_valid(self, form):
        student = form.save()
        msg = 'Студент {0} был добавлен.'.format(student.full_name)
        messages.success(self.request, msg)
        return super(StudentCreateView, self).form_valid(form)

"""		
def create(request):
    if request.method == "post":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, u'Студент {} {} успешно добавлен.'.format(student.name, student.surname))
            return redirect('students:list')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})
"""


class StudentUpdateView(UpdateView):
    model = Student
    
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Student info update"
        return context

    def form_valid(self, form):
        msg = 'Данные изменены.'
        messages.success(self.request, msg)
        return super(StudentUpdateView, self).form_valid(form)
 
"""
 def edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "post":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, u'Данные изменены.')
            return redirect('students:edit', student.id)
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})
"""

class StudentDeleteView(DeleteView):
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

"""
def remove(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "post":
        student.delete()
        messages.success(request, u'Студент {} {} был удален.'.format(student.name, student.surname))
        return redirect('students:list')
    return render(request, 'students/remove.html', {'student': student})
"""