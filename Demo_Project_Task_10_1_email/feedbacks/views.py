# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from feedbacks.forms import FeedbackForm
from django.core.mail import mail_admins
from django.contrib import messages


class FeedbackView(CreateView):
    template_name = 'feedbacks/feedback.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        data = form.cleaned_data
        text = u'Сообщение от {0},\n {1}'.format(data['name'], data['message'])
        mail_admins(data['subject'], text, fail_silently=True)
        messages.success(self.request, u'Сообщение было успешно отправлено')
        return super(FeedbackView, self).form_valid(form)