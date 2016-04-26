# encoding: utf-8
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CourseDetailView(DetailView):
    """ Информация о курсах """
    model = Course
    template_name = "courses/detail.html"
    context_object_name = "course"

    def get_context_data(self,**kwargs):
        context = super(CourseDetailView,self).get_context_data(**kwargs)
        context["title"] = "Course detail"
        pk = self.kwargs['pk']
        context["lessons_list"] = Lesson.objects.filter(course_id = pk)
        return context


class CourseCreateView(CreateView):
    """ Создание нового курса """
    model = Course
    success_url = reverse_lazy('index')
    template_name = "courses/add.html"
    context_object_name = "course"

    def get_context_data(self,**kwargs):
        context = super(CourseCreateView,self).get_context_data(**kwargs)
        context["title"] = "Course creation"
        return context
    
    def form_valid(self,form):
        curs = form.save()
        messages.success(self.request, u'Course %s has been successfully added.'%(curs.name))
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    """ Редактирование данных существующего курса """
    model = Course    
    template_name = "courses/edit.html"
    context_object_name = "course"
    class_form = CourseModelForm

    def get_context_data(self,**kwargs):
        context = super(CourseUpdateView,self).get_context_data(**kwargs)
        context["title"] = "Course update"
        context["pk"] = self.kwargs['pk']
        return context
    
    def form_valid(self,form):
        curs = form.save()
        messages.success(self.request, u'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('courses:detail', kwargs={'pk': pk})


class CourseDeleteView(DeleteView):
    """ Удаление курса с подтверждением """
    model = Course
    success_url = reverse_lazy('students:list_view')
    template_name = "courses/remove.html"
    success_url = reverse_lazy('index')

    def get_context_data(self,**kwargs):
        context = super(CourseDeleteView,self).get_context_data(**kwargs)
        context["title"] = "Course deletion"
        return context
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, u'Course %s has been deleted.'%self.get_object().name)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)


def add_lesson(request,id):
    """ Добавление нового урока для конкретного курса """
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

