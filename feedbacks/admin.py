# -*- coding: cp1251 -*-
from django.contrib import admin
from feedbacks.models import FeedbackForm


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['from_email', 'create_date']

admin.site.register(FeedbackForm, FeedbackAdmin)
