from django.shortcuts import render
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
