# -*- coding: utf-8 -*-
from django import forms
from feedbacks.models import Feedback

class FeedbackModelForm(forms.ModelForm):

    class Meta:
        model = Feedback
