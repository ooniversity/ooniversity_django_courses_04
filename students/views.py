# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm

class SrudentListView(ListView):
    model = Student

    def get_queryset(self):
        course_id = self.request.GET.get('course_id',None)

        if course_id:
            students = Student.objects.filter(courses__id=course_id)
        else:
            students = Student.objects.all()    
        return students


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        student = self.get_object()
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context['title'] = u"Student %s %s detail" % (student.name, student.surname)
        return context





class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:student_list')
    

    def form_valid(self, form):
        message = u"Student %s %s has been successfully added."% (self.object.name, self.object.surname)
        messages.success(self.request, )
        return message

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context    


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:student_list')
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        message = super(StudentUpdateView, self).form_valid(form)
        messages.success(self.request, u"Student %s %s has been successfully updated."% (self.object.name, self.object.surname))
        return message    

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:student_list')

    def form_valid(self, form):
        message = u"Student %s %s has been successfully deleted."% (self.object.name, self.object.surname)
        messages.success(self.request, )
        return message

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context    

'''
def create(request):
    if request.method == "POST":
    	form = StudentModelForm(request.POST)
    	if form.is_valid():
    		application = form.save()
    		message = u"Student %s %s has been successfully added." % (application.name, application.surname)
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
    students = Student.objects.all()
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Студент  был изменен.")
            return render(request, 'students/list_view.html', locals())
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form':form})

def list_view(request):
	course_id = request.GET.get('course_id')

	if course_id:
		students = Student.objects.filter(courses__id=course_id)
	else:
		students = Student.objects.all()	
	return render(request, 'students/list_view.html', locals())


def detail(request, student_id):
	student = Student.objects.get(id=student_id)
	student_courses = student.courses.all()
	return render(request, 'students/detail.html', locals())
'''    
