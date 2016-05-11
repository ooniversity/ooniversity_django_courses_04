# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render,redirect
from datetime import date
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import logging

logger = logging.getLogger(__name__)

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
	
    def get_context_data(self, **kwargs):
    	context = super(StudentDetailView, self).get_context_data(**kwargs)
        logger.debug('Students detail view has been debugged')
        logger.info('Logger of students detail view informs you!')
        logger.warning('Logger of students detail view warns you!')
        logger.error('Students detail view went wrong!')  
        #student = self.get_object()
        #context = super(StudentDetailView, self).get_context_data(**kwargs)
        #context['title'] = u"Student %s %s detail" % (student.name, student.surname)
        return context
   


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        message = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request, u"Student %s %s has been successfully added."
                         % (self.object.name, self.object.surname))
        return message

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

    def get_success_url(self):
        return reverse_lazy('students:edit', kwargs={'pk': self.object.pk})


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        messages.success(self.request, "Info on %s %s has been sucessfully deleted."
                         % (self.object.name, self.object.surname))
        context['title'] = "Student info suppression"
        return context


"""
def detail(request, student_id):
    student = get_object_or_404(Student, id=int(student_id))
    student_courses_list = student.courses.all()
    return render(request, 'students/detail.html', {'student':student, 'students_courses':student_courses_list})

def list_view(request):
    if request.GET:
        course_id = int(request.GET['course_id'])
        course = get_object_or_404(Course, id=course_id)
        list_of_students = course.student_set.all()
        list_of_students.order_by('id')
    else:
        list_of_students = Student.objects.all()
        list_of_students.order_by('id')

    student_courses = dict()
    for stud in list_of_students:
        student_courses[stud.id] = stud.courses.all()
    return render(request, 'students/list.html', {'students_list': list_of_students, 'course_list': student_courses})
    
def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            message =  u"Student %s %s has been successfully added." % (application.name, application.surname)
            messages.success(request, message)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form':form})

def remove(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        message =  u"Info on %s %s has been sucessfully deleted." % (student.name, student.surname)
        student.delete()
        messages.success(request, message)
        return redirect('students:list_view')
    else:
        return render(request, 'students/remove.html', {'student':student})

def edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Info on the student has been sucessfully changed.")
            return render(request, 'students/edit.html', {'form':form})
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form':form})
"""