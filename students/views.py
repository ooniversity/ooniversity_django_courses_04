# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student
from django.utils.datastructures import MultiValueDictKeyError
from forms import StudentModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from students.models import Student



class StudentListView(ListView):
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

"""
def list_view(request):
    try:
        a = request.GET['course_id']
        stud_at_course = Student.objects.filter(courses__id=a)
    except MultiValueDictKeyError:
        stud_at_course = Student.objects.all()
    return render(request, 'students/list.html', {'stud': stud_at_course})
"""


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'

"""
def detail(request, student_id):
    stud_table = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': stud_table})
"""


class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/add.html'
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
    if request.method == 'POST':
        add_form = StudentModelForm(request.POST)
        if add_form.is_valid():
            a = add_form.cleaned_data['name']
            b = add_form.cleaned_data['surname']
            add_form.save()
            msg = 'Студент {0} {1} был добавлен.'.format(a, b)
            messages.success(request, msg)
            return redirect('students:list_view')
    else:
        add_form = StudentModelForm()
    return render(request, 'students/add.html', {'add_s': add_form})
"""


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/edit.html'
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
    edit_app = Student.objects.get(id=pk)
    if request.method == 'POST':
        edit_form = StudentModelForm(request.POST, instance=edit_app)
        if edit_form.is_valid():
            edit_form.save()
            msg = 'Данные изменены.'
            messages.success(request, msg)
    else:
        edit_form = StudentModelForm(instance=edit_app)
    return render(request, 'students/edit.html', {'edit_form': edit_form})
"""


class StudentDeleteView(DeleteView):
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


"""
def remove(request, pk):
    edit_app = Student.objects.get(id=pk)
    context = {}
    context['name'] = edit_app.name
    context['surname'] = edit_app.surname
    if request.method == 'POST':
        edit_app.delete()
        msg = 'Студент {0} {1} был(а) удален(а).'.format(context['name'], context['surname'])
        messages.success(request, msg)

        return redirect('students:list_view')
    return render(request, 'students/remove.html', context)
"""

