# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        course_id = self.kwargs['pk']
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course_id=course_id).order_by('order')
        return context

class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

    def form_valid(self, form):
        messages.set_level(self.request, messages.SUCCESS)
        messages.success(self.request, u'Course {0} has been successfully added.'.format(form.cleaned_data.get('name')))
        return super(CourseCreateView, self).form_valid(form)

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Course update'
        context['pk'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        messages.set_level(self.request, messages.SUCCESS)
        messages.success(self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('courses:edit', kwargs={'pk': pk})

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        messages.set_level(self.request, messages.WARNING)
        messages.warning(self.request, u'Are you sure you want to delete "{0}"?'.format(kwargs['object'].name))
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context

    def delete(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])
        messages.set_level(request, messages.SUCCESS)
        messages.success(request, u'Course {0} has been deleted.'.format(course.name))
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)

class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        lesson = Lesson()
        lesson.course = get_object_or_404(Course, pk=pk)
        lesson.order = Lesson.objects.filter(course=lesson.course).count() + 1
        kwargs['form'] = LessonModelForm(instance=lesson)
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        context['title'] = u'Создание нового занятия'
        return context

    def form_valid(self, form):
        messages.set_level(self.request, messages.SUCCESS)
        messages.success(self.request, u'Lesson {0} has been successfully added.'.format(form.cleaned_data.get('subject')))
        return super(LessonCreateView, self).form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('courses:detail', kwargs={'pk': pk})

def detail(request, course_id):
    course_info = get_object_or_404(Course, id=int(course_id))
    lesson_list = Lesson.objects.filter(course_id=course_id)
    return render(request, 'courses/detail.html', {'lessons':lesson_list, 'course': course_info})

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            curs = form.save()
            messages.success(request, u'Course %s has been successfully added.'%(curs.name))
            return redirect('home')
    else:
        form = CourseModelForm()
    return render(request,"courses/add.html",{"form":form})

def edit(request, id):
    kurs = Course.objects.get(pk = id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance = kurs)
        if form.is_valid():
            kurs = form.save()
            messages.success(request, u'The changes have been saved.')
            return redirect('courses:edit', kurs.id)
                
    else:
        form = CourseModelForm(instance = kurs)
    return render(request,"courses/edit.html",{"form": form})

def remove(request, id):
    kurs = Course.objects.get(pk = id)
    if request.method == 'POST':
        kurs.delete()
        messages.success(request, u'Course %s has been deleted.'%kurs.name)
        return redirect('home')
    return render(request,"courses/remove.html", {"course": kurs})

def add_lesson(request,id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, u'Lesson %s has been successfully added.'%(lesson.subject))
            return redirect('courses:detail', lesson.course.id)
    else:
        course=Course.objects.get(pk=id)
        form = LessonModelForm(initial = {'course': course})
    return render(request,"courses/add_lesson.html",{"form":form})