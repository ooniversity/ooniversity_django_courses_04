 # -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import logging

logger = logging.getLogger(__name__)

class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/detail.html'
	def get_context_data(self, **kwargs):
		context = super(CourseDetailView, self).get_context_data(**kwargs)
		template_name = 'courses/detail.html'
		logger.debug('Courses detail view has been debugged')
		logger.info('Logger of courses detail view informs you!')
		logger.warning('Logger of courses detail view warns you!')
		logger.error('Courses detail view went wrong!')
		return context


#def detail(request, course_id):
#	cours = Course.objects.get(id=course_id)
#	les = Lesson.objects.filter(course_id = course_id)
#	return render(request, 'courses/detail.html', {'cours':cours,'les':les})

class CourseCreateView(CreateView):
	model = Course
	template_name = 'courses/add.html'
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):
		context = super(CourseCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Course creation'
		return context

	def form_valid(self, form):
		course = form.save()
		messages.success(self.request, 'Course %s has been successfully added.' % course.name)
		return super(CourseCreateView, self).form_valid(form)


#def add(request):
#	if request.method == 'POST':
#		form = CourseModelForm(request.POST)
#		if form.is_valid():
#			new_cours = form.save()
#			messages.success(request, 'Course %s has been successfully added.' % new_cours.name)
#			return redirect('/')
#	else:
#		form = CourseModelForm()
#	return render(request, 'courses/add.html', {'form': form})


class CourseUpdateView(UpdateView):
	model = Course
	template_name = 'courses/edit.html'
	def get_context_data(self, **kwargs):
		context = super(CourseUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Course update'
		return context
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'The changes have been saved.')
		return super(CourseUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('courses:edit', args=[self.get_object().id])




#def edit(request, course_id):
#	open_cours = Course.objects.get(id=course_id)
#	if request.method == 'POST':
#		edit_cours = CourseModelForm(request.POST, instance=open_cours)
#		if edit_cours.is_valid():
#			edit_cours.save()
#			messages.success(request, 'The changes have been saved.')
#			return redirect('courses:edit', open_cours.id)
#	else:
#		edit_cours = CourseModelForm(instance=open_cours)
#	return render(request, 'courses/edit.html', {'edit_cours':edit_cours})



class CourseDeleteView(DeleteView):
	model = Course
	template_name = 'courses/remove.html'
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):
		context = super(CourseDeleteView, self).get_context_data(**kwargs)
		context['title'] = 'Course deletion'
		return context

	def delete(self, request, pk):
		course = self.get_object()
		course.delete()
		messages.success(self.request, 'Course %s has been deleted.' % course.name)
		return redirect('index')


#def remove(request, course_id):
#	remove_cours = Course.objects.get(id=course_id)
#	if request.method == 'POST':
#		remove_cours.delete()
#		messages.success(request, 'Course %s has been deleted.' % remove_cours.name)
#		return redirect('/')
#	return render(request, 'courses/remove.html', {'remove_cours':remove_cours})

def add_lesson(request, course_id):
	if request.method == 'POST':
		add_les = LessonModelForm(request.POST)
		if add_les.is_valid():
			new_les = add_les.save()
			messages.success(request, 'Lesson %s has been successfully added.' % new_les.subject)
			return redirect('courses:detail', new_les.course.id)
	else:
		add_les = LessonModelForm()
	return render(request, 'courses/add_lesson.html', {'add_les':add_les})
