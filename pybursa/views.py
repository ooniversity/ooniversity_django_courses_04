# encoding: utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from courses.models import Course


def index(request):
    course_qs = Course.objects.all()
    return render(request, 'index.html',
            {"courses":course_qs})

def contact(request):
    context = [{'name':'Nick Nickolaev',
                'skype':'some.login',
                'email':'somemail@gmail.com',
                'phone':'+38 099 000 00 02',
                'lvl':'Director'
                },
                {'name':'Дария Михалевич',
                'skype':'darka.darka.darka.darka.',
                'email':'daria.mykhalevych@gmail.com',
                'phone':'+38 096 469 15 57',
                'lvl':'Manager'
                },
              {'name':'Павел Обод',
            'skype':'azaless',
            'email':'tbursa100@gmail.com',
            'phone':'+38 099 000 00 01',
            'lvl':'Founder'
            }]

    return render(request, 'contact.html', {"contacts":context})

def student_detail(request):
    return render(request, 'student_detail.html')


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
