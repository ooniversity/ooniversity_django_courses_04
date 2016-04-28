# -*- coding: utf-8 -*-
from django.shortcuts import render
from feedbacks.models import Feedback
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy


class FeedbackView(CreateView):
	model = Feedback
	template_name = "feedback.html"
	success_url = reverse_lazy('feedback')




