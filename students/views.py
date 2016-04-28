# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student
from forms import StudentModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class StudentListView(ListView):
	model = Student
	context_object_name = 'deskr'
	paginate_by = 2
	def get_queryset(self):
		if self.request.GET:
			deskr = Student.objects.filter(courses__id=int(self.request.GET['course_id']))
		else:
			deskr = Student.objects.all()
		return deskr

#def list_view(request):
#	if request.GET:
#		deskr = Student.objects.filter(courses__id=int(request.GET['course_id']))
#	else:
#		deskr = Student.objects.all()
#	return render(request, 'students/list.html', {'deskr':deskr})




class StudentDetailView(DetailView):
	model = Student

#def detail(request, student_id):
#	det = Student.objects.get(id=student_id)
#	return render(request, 'students/detail.html', {'det':det})




class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Student registration'
		return context
	def form_valid(self, form):
		message = super(StudentCreateView, self).form_valid(form)
		messages.success(self.request, "Student %s %s has been successfully added." % (self.object.name, self.object.surname))
		return message




#def create(request):
#	if request.method == 'POST':
#		form = StudentModelForm(request.POST)
#		if form.is_valid():
#			create_st = form.save()
#			messages.success(request, "Student %s %s has been successfully added." % (create_st.name, create_st.surname))
#			return redirect('students:list_view')
#	else:
#		form = StudentModelForm()
#	return render(request, 'students/add.html', {'form':form})





class StudentUpdateView(UpdateView):
	model = Student

	def form_valid(self, form):
		messages.success(self.request, 'Данные изменены')
		return super(StudentUpdateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Student info update'
		return context

	def get_success_url(self):
		return reverse_lazy('students:edit', kwargs={'pk':self.object.pk})



#def edit(request, student_id):
#	edit_st = Student.objects.get(id=student_id)
#	if request.method == 'POST':
#		form = StudentModelForm(request.POST, instance=edit_st)
#		if form.is_valid():
#			form.save()
#			messages.success(request, 'Данные изменены')
#			return redirect('students:edit', student_id)
#	else:
#		form = StudentModelForm(instance=edit_st)
#	return render(request, 'students/edit.html', {'form':form})



class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students:list_view')
	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = 'Student info suppression'
		return context

	def form_valid(self, form):
		messages.success(self.request, "Info on %s %s has been successfully deleted." % (self.object.name, self.object.surname))
		return super(StudentUpdateView, self).form_valid(form)




#def remove(request, student_id):
#	remov = Student.objects.get(id=student_id)
#	if request.method == 'POST':
#		remov.delete()
#		messages.success(request, "Info on %s %s has been successfully deleted." % (remov.name, remov.surname))
#		return redirect('students:list_view')
#	return render(request, 'students/remove.html', {'remov':remov})
