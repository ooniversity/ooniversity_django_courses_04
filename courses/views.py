from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
import logging

from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'details'

    def get_context_data(self, **kwargs):
        logger.debug("Courses detail view has been debugged")
        logger.warning("Logger of courses detail view informs you!")
        logger.info("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lesson'] = Lesson.objects.filter(course__id=self.kwargs['pk'])
        return context


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/add.html'


    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        course = form.save()
        messages.success(self.request, "Course %s has been successfully added." % course)
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'


    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def form_valid(self, form):
        messages.success(self.request, "The changes have been saved.")
        return super(CourseUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('courses:edit', kwargs={'pk': self.object.pk})


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'


    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, *args, **kwargs):
        context = super(CourseDeleteView, self).delete(self.request, *args, **kwargs)
        messages.success(self.request, "Course %s has been deleted." % self.object)
        return context
  

def add_lesson(request, course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson_name = form.cleaned_data["subject"]
            form.save()
            messages.success(request, "Lesson %s has been successfully added." % lesson_name)
            return redirect("courses:detail", course_id=course_id)
    else:
        form = LessonModelForm(initial={'course': course_id})

    return render(request, "courses/add_lesson.html", {'form': form})