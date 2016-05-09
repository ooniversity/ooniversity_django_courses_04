from django.shortcuts import get_object_or_404, render, render_to_response
from courses.models import Course

# Create your views here.
#from django.http import Http404, HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
#from django.views import generic

courses = Course.objects.all()
def index(request):
    return render(request, 'index.html', {'courses': courses})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')

def custom_404(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response


def custom_500(request):
    response = render_to_response('500.html')
    response.status_code = 500
    return response
