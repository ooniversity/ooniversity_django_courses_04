from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import mail_admins
from models import Feedback

class FeedbackView(CreateView):
	model = Feedback
	template_name = 'feedback/feedback.html'
	success_url = reverse_lazy('feedback')



	def form_valid(self, form):
		mail = form.save()
		mail_admins(mail.subject, mail.message)
		messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
		return super(FeedbackView, self).form_valid(form)
