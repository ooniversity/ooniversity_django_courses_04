from django.shortcuts import render
from django.views.generic.edit import CreateView
from feedbacks.models import Feedback
from django.core.mail import mail_admins
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        valid = super(FeedbackView, self).form_valid(form)
        if valid:
            mail = form.cleaned_data
            mail_admins(mail['subject'], mail['message'], fail_silently=False, connection=None, html_message=None)
            messages.success(self.request, u"Thank you for your feedback! We will keep in touch with you very soon!")
        return valid