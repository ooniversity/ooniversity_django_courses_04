from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
from django.views.generic import TemplateView
from django.views.generic.base import View

class MixinCoachContext(object):
	
	def get_context_data(self,**kwargs):
		context = super(MixinCoachContext, self).get_context_data(**kwargs)
		context['coach'] = Coach.objects.get(id = kwargs['coach_id'])		
		context['teacher'] = Course.objects.filter(coach = kwargs['coach_id'])		
		context['assistant'] = Course.objects.filter(assistant = kwargs['coach_id'])		
		return context

class CoachesDetailView(MixinCoachContext, TemplateView):
	template_name = 'coaches/detail.html'
