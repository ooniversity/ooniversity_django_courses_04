# encoding: utf-8
from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
from django.views.generic.detail import DetailView


class CoachDetailView(DetailView):
    """ Информация о преподавателе """
    model = Coach
    template_name = "coaches/detail.html"

    def get_context_data(self, **kwargs):
        context = super(CoachDetailView,self).get_context_data(**kwargs)
        context["title"] = u"Информация о преподавателе"
        return context
    

