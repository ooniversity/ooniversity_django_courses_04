from django.shortcuts import render


def index(request):
    """
    Call index.html
    """
    return render(request, 'index.html')


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


