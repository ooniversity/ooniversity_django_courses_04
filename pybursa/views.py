# encoding: utf-8
from django.shortcuts import render
from django.views.generic.edit import CreateView#, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail

from courses.models import Course
from students.models import Student
from feedbacks.models import Feedback
from pybursa.settings import ADMINS


def index(request):
    course_qs = Course.objects.all()
    return render(request, 'index.html',
            {"courses":course_qs})

def contact(request):
    return render(request, 'contact.html')

def student_detail(request):
    return render(request, 'student_detail.html')

class FeedbackView(CreateView):
    """docstring for FeedbackView"""
    model = Feedback
    # context_object_name = 'course'
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def get_context_data(self, **kwargs):
        context = super(FeedbackView,self).get_context_data(**kwargs)
        context['title'] = 'Feedback'
        return context

    def form_valid(self, form):
        mail_form = form.save()
        mail_to = []
        for name, mail in ADMINS:
            mail_to.append(mail)
        send_mail(mail_form.subject, mail_form.message, mail_form.from_email, mail_to, fail_silently = False)
        message =  u"Thank you for your feedback! We will keep in touch with you very soon!"
        messages.success(self.request, message)
        return super(FeedbackView, self).form_valid(form)
