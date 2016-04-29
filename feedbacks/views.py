# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView

from feedbacks.models import Feedback
from pybursa.settings import ADMINS

class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def get_context_data(self, **kwards):
        context = super(FeedbackView, self).get_context_data(**kwards)
        context['title'] = 'Feedback'
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        messages.set_level(self.request, messages.SUCCESS)
        messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
        send_mail(data.get('subject'), data.get('message'), data.get('from_email'), [item[1] for item in ADMINS], fail_silently=False)
        return super(FeedbackView, self).form_valid(form)
