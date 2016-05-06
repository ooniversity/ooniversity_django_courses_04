# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

import logging
logger = logging.getLogger(__name__)  #students.views

class StudentDetailView(DetailView):
	model = Student

	def get_context_data(self, **kwargs):
		context = super(StudentDetailView, self).get_context_data(**kwargs)
		logger.debug("Students detail view has been debugged")
		logger.info("Logger of students detail view informs you!")
		logger.warning("Logger of students detail view warns you!")
		logger.error("Students detail view went wrong!")
		return context

class StudentListView(ListView):
	model = Student
	paginate_by = 2
	
	#def get_queryset(self):
	#	if self.request.GET:
	#		course_id = self.request.GET['course_id']
	#		students = Student.objects.filter(courses=course_id).order_by('id')	
	#	else:
	#		students = Student.objects.all()
	#	return students
	def get_queryset(self):
		qs = super(StudentListView, self).get_queryset()
		course_id = self.request.GET.get('course_id', None)
		if course_id:
			qs = qs.filter(courses=course_id)
		return qs
	

class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = u'Student registration'
		return context

	def form_valid(self, form):
		application = form.save()
		message = u'Student %s %s has been successfully added.' % (application.name, application.surname)
		messages.success(self.request, message)
		return super(StudentCreateView, self).form_valid(form)
		

class StudentUpdateView(UpdateView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = u'Student info update'
		return context

	def form_valid(self, form):
		application = form.save()
		message = u'Info on the student has been sucessfully changed.'
		messages.success(self.request, message)
		return super(StudentUpdateView, self).form_valid(form)

class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = u'Student info suppression'
		return context

	#def form_valid(self, form):
	#	application = form.save()
	#	message = u'Info on %s %s has been sucessfully deleted.' % (application.name, application.surname)
	#	messages.success(self.request, message)
	#	print "DELETE MY OBJECT!"
	#	return super(StudentDeleteView, self).form_valid(form)

def create(request):	
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			message = u'Student %s %s has been successfully added.' % (application.name, application.surname)
			messages.success(request, message)
			return redirect('students:list_view')
	else:
		form = StudentModelForm()

	return render(request,'students/add.html', {'form':form})	


def edit(request, id):
	application = Student.objects.get(id=id)
	if request.method == 'POST':
		form = StudentModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			message = u'Info on the student has been sucessfully changed.'
			messages.success(request, message)			
	else:
		form = StudentModelForm(instance=application)

	return render(request,'students/edit.html', {'form':form})


def remove(request, id):
	application = Student.objects.get(id=id)
	if request.method == 'POST':
		application.delete()
		message = u'Info on %s %s has been sucessfully deleted.' % (application.name, application.surname)
		messages.success(request, message)
		return redirect('students:list_view')
	
	return render(request,'students/remove.html', {'ap':application})


def list_view(request):	
	if request.GET:
		course_id = request.GET['course_id']
		students = Student.objects.filter(courses=course_id).order_by('id')	
	else:
		students = Student.objects.all()
	
	return render(request, 'students/list.html', {'students':students})


def student_detail(request, id):
	student = Student.objects.get(id=id)
	return render(request, 'students/detail.html', {'student':student})
	message = u'Info on %s %s has been sucessfully deleted.' % (application.name, application.surname)
