from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = "courses/add.html"
    context_object_name = "c_list"

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        application = form.save()
        message =  u"Course %s has been successfully added." % application.name
        messages.success(self.request, message)
        return super(CourseCreateView, self).form_valid(form)
    
class CourseUpdateView(UpdateView):
    model = Course
    template_name = "courses/edit.html"
    context_object_name = "c_list"

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def form_valid(self, form):
        form.save()
        message =  u"The changes have been saved."
        messages.success(self.request, message)
        return super(CourseUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('courses:edit', args=[self.get_object().id])

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = "courses/remove.html"
    context_object_name = "c_list"

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, pk):
        course = self.get_object()
        message =  u"Course %s has been deleted." % course.name
        course.delete()
        messages.success(self.request, message)
        return redirect('index')

class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"
    context_object_name = "co_urse"

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

#def add_lesson(request, course_id):
#    if request.method == "POST":
#        form = LessonModelForm(request.POST)
#        if form.is_valid():
#            lesson = form.save()
#            message =  u"Lesson %s has been successfully added." % lesson.subject
#            messages.success(request, message)
#            return redirect("courses:detail", lesson.course.id)
#    else:
#        form = LessonModelForm(initial = {'course':course_id})
#    return render(request, 'courses/add_lesson.html', {'form':form})

#def detail(request, course_id):
#    course_info = get_object_or_404(Course, id=int(course_id))
#    lesson_list = Lesson.objects.filter(course_id=course_id)
#    return render(request, 'courses/detail.html', {'lessons':lesson_list, 'course': course_info})

#def add(request):
#   if request.method == "POST":
#        form = CourseModelForm(request.POST)
#        if form.is_valid():
#            application = form.save()
#            message =  u"Course %s has been successfully added." % application.name
#            messages.success(request, message)
#            return redirect('/')
#    else:
#        form = CourseModelForm()
#    return render(request, 'courses/add.html', {'form':form})

#def edit(request, course_id):
#    course = get_object_or_404(Course, id = course_id)
#    if request.method == "POST":
#        form = CourseModelForm(request.POST, instance = course)
#        if form.is_valid():
#            course_form = form.save()
#            messages.success(request, u"The changes have been saved.")
#            return redirect('courses:edit', course_form.id)
#    else:
#        form = CourseModelForm(instance = course)
#    return render(request, 'courses/edit.html', {'form':form})

#def remove(request, course_id):
#    course = get_object_or_404(Course, id  =course_id)
#    if request.method == "POST":
#        message =  u"Course %s has been deleted." % course.name
#        course.delete()
#        messages.success(request, message)
#        return redirect('/')
#    else:
#        return render(request, 'courses/remove.html', {'course':course})