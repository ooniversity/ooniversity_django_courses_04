from django.conf.urls import patterns
from django.conf.urls import url

from feedbacks import views


urlpatterns = patterns('',

    url(r'^$', views.FeedbackView.as_view(), name='feedback'),

)
