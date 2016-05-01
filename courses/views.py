from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.core.urlresolvers import reverse_lazy, reverse

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        course_id = self.object.id
        context['lessons'] = Lesson.objects.filter(course_id=course_id)
        context['title'] = 'Course  Detail'
        return context

#def detail(request, course_id):
#    course = Course.objects.get(id=course_id)
#    lessons = Lesson.objects.filter(course_id=course_id)
#    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons})

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('index')
    success_message = "Course %(name)s has been successfully added."
    template_name = 'courses/add.html'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

#def add(request):
#    if request.method == 'POST':
#        form = CourseModelForm(request.POST)
#        if form.is_valid:
#            item = form.save()
#            messages.success(request, "Course %s has been successfully added." % item.name)
#            return redirect('index')
#    else:
#        form = CourseModelForm()
#    return render(request, "courses/add.html", {'form': form})

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
#    success_url = reverse_lazy('courses:edit', self.object.id)
    success_url = reverse_lazy('index')
    success_message = "The changes have been saved."
    template_name = 'courses/edit.html'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

def edit(request, course_id):
    item = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            messages.success(request, "The changes have been saved.")
        return redirect('courses:edit', course_id)
    else:
        form = CourseModelForm(instance=item)
    return render(request, "courses/edit.html", {'form': form})

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    success_message = "Course %(name)s has been deleted."
    template_name = 'courses/remove.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context

#def remove(request, course_id):
#    item = Course.objects.get(id=course_id)
#    if request.method == 'POST':
#        item.delete()
#        messages.success(request, "Course %s has been deleted." % item.name)
#        return redirect('index')
#    return render(request, "courses/remove.html", {'item': item})

class LessonCreateView(CreateView):
    model = Lesson
    template_name = "courses/add_lesson.html"


    def get_context_data(self, **kwargs):
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        context['title'] = "Lesson creation"
        return context


    def form_valid(self, form):
        item = form.save()
        messages.success(self.request, u"Lesson %s has been successfully added" % item.subject)
        return super(LessonCreateView, self).form_valid(form)


    def get_success_url(self):
        #pk = self.kwargs['pk']
        self.success_url = reverse('courses:detail', kwargs={'pk': self.object.course.id})
        return self.success_url

#def add_lesson(request, course_id):
#    if request.method == 'POST':
#        form = LessonModelForm(request.POST)
#        if form.is_valid:
#            item = form.save()
#            messages.success(request, "Lesson %s has been successfully added" % item.subject)
#            return redirect("courses:detail", course_id)
#    else:
#        form = LessonModelForm(initial={'news_subscribe':True, 'course': course_id})
#    return render(request, "courses/add_lesson.html", {'form': form})


