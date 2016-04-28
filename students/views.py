# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


''' begin Class-based views '''

class StudentListView(ListView):
    model = Student    

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students_list = Student.objects.filter(courses__id=course_id)
            students_list.order_by('id')
        else:
            students_list = Student.objects.all()
            students_list.order_by('id')
        return students_list

class StudentDetailView(DetailView):
    model = Student    

class  StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context["title"] = "Student registration"
        return context
    
    def form_valid(self,form):
        application = form.save()
        messages.success(self.request, u'Student %s %s has been successfully added.'%(application.name, application.surname))
        return super(StudentCreateView, self).form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Student info update"
        return context
    
    def form_valid(self,form):
        application = form.save()
        messages.success(self.request, u'Info on the student has been sucessfully changed.')
        return super(StudentUpdateView, self).form_valid(form)

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context["title"] = "Student info suppression"
        return context


''' end Class-based views '''

'''
def list_view(request):
    if request.GET:
        course_id = int(request.GET['course_id'])
        course = get_object_or_404(Course, id=course_id)
        students_list = course.student_set.all()
        students_list.order_by('id')
    else:
        students_list = Student.objects.all()
        students_list.order_by('id')

    student_courses = dict()

    for st in students_list:
        student_courses[st.id] = st.courses.all()
        s = {
             'students_list': students_list, 
             'course_list': student_courses
             }
    return render(request, 'students/student_list.html', s)


def detail(request, student_id):
    student = get_object_or_404(Student, id=int(student_id))
    student_courses_list = student.courses.all()
    s = {
         'student':student, 
         'students_courses':student_courses_list
        }
    return render(request, 'students/detail.html', s)


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, u'Student %s %s has been successfully added.' % (application.name, application.surname))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form' : form})


def remove(request, student_id):
    student_inst = get_object_or_404(Student, id=student_id)    
    if request.method == 'POST':
        messages.success(request, u'Info on %s %s has been sucessfully deleted.' % (student_inst.name, student_inst.surname))
        student_inst.delete()
        return redirect('students:list_view')
    return render(request,'students/remove.html', {'student': student_inst})


def edit(request, student_id):    
    student_inst = get_object_or_404(Student, id=student_id)    
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance = student_inst)
        if form.is_valid():
            form.save()
            messages.success(request, u'Info on the student has been sucessfully changed.')
            return redirect('students:list_view')                
    else:
        form = StudentModelForm(instance = student_inst)
    return render(request, 'students/edit.html', {'form': form})

'''
