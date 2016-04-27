from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.kwargs['pk'])
        return context

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        valid = super(CourseCreateView, self).form_valid(form)
        if valid:
            course = self.request.POST
            message = u"Course {} has been successfully added."
            messages.success(self.request, message.format(course['name']))
        return valid

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/edit.html'
    
    def get_success_url(self):
         return reverse("courses:edit", kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        valid = super(CourseUpdateView, self).form_valid(form)
        if valid:
            message = "The changes have been saved."
            messages.success(self.request, message)
        return valid

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        message = u"Course {} has been deleted."
        messages.success(self.request, message.format(course.name))
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

def add_lesson(request,id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            message = u"Lesson {} has been successfully added."
            messages.success(request, message.format(lesson.subject))
            return redirect('courses:detail', lesson.course.id)
    else:
        form = LessonModelForm(initial={'course': id})
        return render(request, "courses/add_lesson.html", {"form": form})