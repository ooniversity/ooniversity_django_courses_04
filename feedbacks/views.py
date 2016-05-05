from django.shortcuts import render
from feedbacks.models import Feedback
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages
from pybursa.settings import ADMINS


class FeedbackView(CreateView):
    model = Feedback
    fields = '__all__' # if empty - rise an error "RemovedInDjango18Warning: Calling modelform_factory...'fields' or 'exclude'..." 
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        data = form.cleaned_data
        destination = [mail[1] for mail in ADMINS]
        send_mail(data['subject'], data['message'], data['from_email'],
                  destination, fail_silently=False)
        notice = u"Thank you for your feedback! We will keep in touch with you very soon!"
        messages.success(self.request, notice)
        return super(FeedbackView, self).form_valid(form)