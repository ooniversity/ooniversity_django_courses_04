from datetime import datetime

from django.core.urlresolvers import reverse_lazy
from django.core.mail import mail_admins
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib import messages

from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm

from pybursa.settings import ADMINS

class FeedbackView(CreateView):
    model = Feedback
    template_name = "feedback.html"
    success_url = reverse_lazy('feedback')
        

    def get(self, request):
        class_form = FeedbackForm()
        return render(request, self.template_name, {"form":class_form})

    def form_valid(self,form):
        fback = form.save()
        mail_admins(fback.subject, fback.message, fail_silently=False)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return super(FeedbackView, self).form_valid(form)
