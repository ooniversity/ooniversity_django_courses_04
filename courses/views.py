# encoding: utf-8
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

class MixinAuthor(object):
    """
    добавляю в контекст автора кода (только для реализации миксина)
    """
    def get_context_data(self,**kwargs):
        context = super(MixinAuthor, self).get_context_data(**kwargs)
        context['code_writer'] = "Проскурин Александр"
        return context

        
class MixinPaginator(MultipleObjectMixin):
    """
    Реализация пагинатора, при отсутствии таковой возможности в CBV класса родителя
    """
    object_list = None
    
    def get_paginator(self, queryset, per_page, orphans, allow_empty_first_page):
        pag = super(MixinPaginator, self).get_paginator(queryset, per_page, orphans, allow_empty_first_page)
        #self.get_context_data(self.kwargs)
        return pag
    
    def paginate_queryset(self, queryset, page_size):
        preq = super(MixinPaginator, self).paginate_queryset(queryset, page_size)
        #self.get_context_data(**self.kwargs)
        return preq
    
    def get_context_data(self, **kwargs):
        context = super(MixinPaginator, self).get_context_data(**kwargs)
        context["paginator"] = self.object_list
        return context
        
        
class CourseDetailView(DetailView, MixinPaginator):
    """ Информация о курсах """
    model = Course
    template_name = "courses/detail.html"
    context_object_name = "course"
    success_url = reverse_lazy('index')
        
    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context["title"] = "Course detail"
        pk = self.kwargs['pk']
        paginator_obj = self.get_paginator(Lesson.objects.filter(course__id = pk), 5, 0, True)
        page = self.request.GET.get('page',1)
        context["lessons_list"] = paginator_obj.page(page)
        context["page"] = paginator_obj.page(page)
        return context

    def get_request(self):
        req = super(CourseDetailView, self).get_request()
        return req    

class CourseCreateView(CreateView):
    """ Создание нового курса """
    model = Course
    success_url = reverse_lazy('index')
    template_name = "courses/add.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context["title"] = "Course creation"
        return context
    
    def form_valid(self, form):
        curs = form.save()
        messages.success(self.request, u'Course %s has been successfully added.'%(curs.name))
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(MixinAuthor, UpdateView):
    """ Редактирование данных существующего курса """
    model = Course    
    template_name = "courses/edit.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Course update"
        context["pk"] = self.kwargs['pk']
        return context
    
    def form_valid(self, form):
        curs = form.save()
        messages.success(self.request, u'The changes have been saved.')
        self.success_url = reverse('courses:edit', kwargs={'pk': curs.id})
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    """ Удаление курса с подтверждением """
    model = Course
    success_url = reverse_lazy('students:list_view')
    template_name = "courses/remove.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context["title"] = "Course deletion"
        return context
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, u'Course %s has been deleted.'%self.get_object().name)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)

        
class LessonCreateView(CreateView):
    """ Добавление нового урока для конкретного курса """
    model = Lesson
    template_name = "courses/add_lesson.html"
    
    def get(self, request, *args, **kwargs):
        course = Course.objects.get(pk = self.kwargs['pk'])
        class_form = LessonModelForm(initial = {'course': course})
        return render(request, self.template_name, {"form":class_form})
        
    def get_context_data(self, **kwargs):
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        context["title"] = "Lesson creation"
        return context
    
    def form_valid(self, form):
        lesson = form.save()
        messages.success(self.request, u'Lesson %s has been successfully added.'%(lesson.subject))
        self.success_url = lesson.get_absolute_url()
        return super(LessonCreateView, self).form_valid(form)
