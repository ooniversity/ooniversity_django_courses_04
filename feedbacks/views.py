from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail

from django.views.generic.edit import CreateView

from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm

from pybursa.settings import ADMINS

class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        mail_form = form.save()
        mail_to = list()
        for name, mail in ADMINS:
            mail_to.append(mail)
        send_mail(mail_form.subject, mail_form.message, mail_form.from_email, mail_to, fail_silently = False)
        message =  u"Thank you for your feedback! We will keep in touch with you very soon!"
        messages.success(self.request, message)
        return super(FeedbackView, self).form_valid(form)
