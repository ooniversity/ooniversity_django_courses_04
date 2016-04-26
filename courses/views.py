# encoding: utf-8
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy


class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/detail.html'
	context_object_name = 'course'

	def get_context_data(self, **kwargs):
		context = super(CourseDetailView,self).get_context_data(**kwargs)
		context["title"] = "Course detail"
		pk = self.kwargs['pk']
		context["lesson"] = Lesson.objects.filter(course_id = pk)
		return context

class CourseCreateView(CreateView):
	model = Course
	template_name = 'courses/add.html'
	context_object_name = 'course'
	success_url = reverse_lazy('index')

	def get_context_data(self,**kwargs):
		context = super(CourseCreateView, self).get_context_data(**kwargs)
		context['title'] = u"Course creation"
		return context

	def form_valid(self,form):
		course = form.save()
		messages.success(self.request, u" Course %s has been successfully added." %(course.name))
		return super(CourseCreateView, self).form_valid(form)

class CourseUpdateView(UpdateView):
	model = Course
	template_name = 'courses/edit.html'
	context_object_name = 'course'
	
	def get_context_data(self,**kwargs):
		context = super(CourseUpdateView, self).get_context_data(**kwargs)
		context["pk"] = self.kwargs['pk']
		context['title'] = u"Course update"
		return context

	def form_valid(self,form):
		course = form.save()
		messages.success(self.request, u'The changes have been saved.')
		return super(CourseUpdateView, self).form_valid(form)

	def get_success_url(self):
		pk = self.kwargs['pk']
		return reverse('courses:edit', kwargs={'pk': pk})

class CourseDeleteView(DeleteView):
	model = Course
	template_name = 'courses/remove.html'
	context_object_name = 'course'
	success_url = reverse_lazy('index')

	def get_context_data(self,**kwargs):
		context = super(CourseDeleteView, self).get_context_data(**kwargs)
		context['title'] = u"Course deletion"
		return context

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, u'Course %s has been deleted.'%self.get_object().name)
		return super (CourseDeleteView, self).delete(request, *args, **kwargs)

def create(request):
	if request.method == 'POST':
		form = CourseModelForm(request.POST)
		if form.is_valid():
			course = form.save()
			message = u" Course %s has been successfully added." %(course.name)
			messages.success(request, message)
			return redirect("index")
	else:
		form = CourseModelForm()

	return render(request, 'courses/add.html', {'form':form})


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
        return redirect('index')
    return render(request,"courses/remove.html", {"course": kurs})



def add_lesson(request,id):
	if request.method == 'POST':
		form = LessonModelForm(request.POST)
		if form.is_valid():
			lesson = form.save()
			message = u"Lesson %s has been successfully added." %(lesson.subject)
			messages.success(request, message)
			return redirect('courses:detail', lesson.course.id)
	else:


		course=Course.objects.get(pk=id)
		form = LessonModelForm(initial = {'course': course})
	return render(request, 'courses/add_lesson.html', {"form":form})


def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lesson = Lesson.objects.filter(course_id = course_id)
    return render(request, 'courses/detail.html',{'course':course, 'lesson':lesson})




