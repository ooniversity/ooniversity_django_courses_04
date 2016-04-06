from django.shortcut import render
from django.template import RequestContext, loader

def index(request):
    #template = loader.get_template('index.html')
    return render(request, 'index.html')



def contact(request):

    return render(request, 'contact.html')


def student_list(request):

    return render(request, 'student_list.html')


def student_detail(request):

    return render(request, 'student_detail.html')