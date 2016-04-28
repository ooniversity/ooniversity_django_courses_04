from django.shortcuts import render
from django.views.generic.edit import CreateView
from feedbacks.models import Feedback
from django.core.urlresolvers import reverse_lazy 
from django.core.mail import mail_admins
from django.contrib import messages

class FeedbackView(CreateView):
	model = Feedback
	template_name = 'feedback.html'
	success_url = reverse_lazy('feedback')

	def get_context_data(self, **kwargs):
		context = super(FeedbackView, self).get_context_data(**kwargs)
		context['title'] = u'Feedback creation'		
		return context

	def form_valid(self, form):
		feedback = form.save()
		mail_admins(feedback.subject, feedback.message, fail_silently=False)		
		message = u'Thank you for your feedback! We will keep in touch with you very soon!'
		messages.success(self.request, message)
		return super(FeedbackView, self).form_valid(form)
