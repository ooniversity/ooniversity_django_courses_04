 # -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from forms import CourseModelForm, LessonModelForm
from django.contrib import messages

def detail(request, course_id):
	cours = Course.objects.get(id=course_id)
	les = Lesson.objects.filter(course_id = course_id)
	return render(request, 'courses/detail.html', {'cours':cours,'les':les})


def add(request):
	if request.method == 'POST':
		form = CourseModelForm(request.POST)
		if form.is_valid():
			new_cours = form.save()
			messages.success(request, 'Course %s has been successfully added.' % new_cours.name)
			return redirect('/')
	else:
		form = CourseModelForm()
	return render(request, 'courses/add.html', {'form': form})


def edit(request, course_id):
	open_cours = Course.objects.get(id=course_id)
	if request.method == 'POST':
		edit_cours = CourseModelForm(request.POST, instance=open_cours)
		if edit_cours.is_valid():
			edit_cours.save()
			messages.success(request, 'The changes have been saved.')
			return redirect('courses:edit', open_cours.id)
	else:
		edit_cours = CourseModelForm(instance=open_cours)
	return render(request, 'courses/edit.html', {'edit_cours':edit_cours})


def remove(request, course_id):
	remove_cours = Course.objects.get(id=course_id)
	if request.method == 'POST':
		remove_cours.delete()
		messages.success(request, 'Course %s has been deleted.' % remove_cours.name)
		return redirect('/')
	return render(request, 'courses/remove.html', {'remove_cours':remove_cours})

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
