from django.shortcuts import render, render_to_response
from courses.models import Course


def index(request):
    """
    Call index.html
    """
    params = {'courses': Course.objects.all()}
    return render(request, 'index.html', params)


def contact(request):
    """
    Call contact.html
    """
    return render(request, 'contact.html')


def student_list(request):
    """
    Call student_list.html
    """
    return render(request, 'student_list.html')


def student_detail(request):
    """
    Call student_detail.html
    """
    return render(request, 'student_detail.html')


def custom_404_server_error(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response


def custom_500_server_error(request):
    response = render_to_response('500.html')
    response.status_code = 500
    return response