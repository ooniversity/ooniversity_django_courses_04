#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm


class FeedbackView(CreateView):
    model = Feedback
    #form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form): 
        self.application = form.save()
        send_mail(self.application.subject, self.application.message, self.application.from_email, ['olshilyaeva@gmail.com'], fail_silently=False)       
        messages.success(self.request, u'Thank you for your feedback! We will keep in touch with you very soon!')
        return super(FeedbackView, self).form_valid(form)   


