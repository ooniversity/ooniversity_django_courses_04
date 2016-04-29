from courses.models import Course, Lesson
from django.contrib import messages
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
 
class CourseDetailView(DetailView):
	model = Course
	template_name = "courses/detail.html"
	context_object_name = "course"
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):
		context = super(CourseDetailView, self).get_context_data(**kwargs)
		context['title'] = u'Course detail'
		pk = self.kwargs['pk']
 		context['lessons'] = Lesson.objects.filter(course_id=pk)
 		return context
 
class CourseCreateView(CreateView):
	model = Course
 	template_name = "courses/add.html"
 	context_object_name = "course"
 	success_url = reverse_lazy('index')
 
	def get_context_data(self, **kwargs):
 		context = super(CourseCreateView, self).get_context_data(**kwargs)
 		context['title'] = u'Course creation'		
 		return context
 
 	def form_valid(self, form):
 		application = form.save()
 		message = u'Course %s has been successfully added.' % (application.name)
 		messages.success(self.request, message)
 		return super(CourseCreateView, self).form_valid(form)
 
class CourseUpdateView(UpdateView):
 	model = Course
 	template_name = "courses/edit.html"
 	context_object_name = "course"
 	
 
 	def get_context_data(self, **kwargs):
 		context = super(CourseUpdateView, self).get_context_data(**kwargs)
 		context['title'] = u'Course update'		
 		return context
 
 	def form_valid(self, form):
 		application = form.save()
 		message = u'The changes have been saved.'
 		messages.success(self.request, message)
 		return super(CourseUpdateView, self).form_valid(form)
 
 	def get_success_url(self):
 		pk = self.kwargs['pk']
 		self.success_url = reverse('courses:edit', kwargs={'pk':pk})
 		return self.success_url
 
 
class CourseDeleteView(DeleteView):
 	model = Course
 	template_name = "courses/remove.html"
 	context_object_name = "course"
 	success_url = reverse_lazy('index')
 
	def get_context_data(self, **kwargs):
 		context = super(CourseDeleteView, self).get_context_data(**kwargs)
 		context['title'] = u'Course deletion'		
 		return context
 
	def delete(self, request, *args, **kwargs):		
 		message = u'Course %s has been deleted.' % self.get_object().name
 		messages.success(self.request, message)
 		return super(CourseDeleteView, self).delete(request, *args, **kwargs)
		
class MixinLessonContext(object):
    def get_context_data(self, **kwargs):
        context = super(MixinLessonContext, self).get_context_data(**kwargs)
        context['title'] = u"Lesson creation"
        return context
 
class LessonCreateView(MixinLessonContext, CreateView):
    model = Lesson
    template_name = "courses/add_lesson.html"
 
    def form_valid(self, form):
        lesson = form.save()
        message =  u"Lesson %s has been successfully added." % lesson.subject
        messages.success(self.request, message)
        return super(LessonCreateView, self).form_valid(form)