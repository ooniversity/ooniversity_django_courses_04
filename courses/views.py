from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.shortcuts import render, redirect

from courses.models import Course
from courses.forms import LessonModelForm


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/detail.html'


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request,
                         "Course %s has been successfully added." %
                         form.cleaned_data['name'])
        return super(CourseCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'

    def form_valid(self, form):
        messages.success(self.request, "The changes have been saved.")
        self.success_url = reverse('courses:edit', args=(form.instance.id,))
        return super(CourseUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        messages.success(self.request, "Course %s has been deleted." %
                         course.name)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context


def add_lesson(request, course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            message = u"Lesson %s has been successfully added." % \
                      lesson.subject
            messages.success(request, message)
            return redirect("courses:detail", lesson.course.id)
    else:
        form = LessonModelForm(initial={'course': course_id})
    return render(request, 'courses/add_lesson.html', {'form': form})
