from django.shortcuts import render, render_to_response
from courses.models import Course


def index(request):
    
    courses_list = Course.objects.all()
    return render(request, 'index.html', {'courses_list': courses_list})


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')


def server_error_404(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response


def server_error_500(request):
    response = render_to_response('500.html')
    response.status_code = 500
    return response