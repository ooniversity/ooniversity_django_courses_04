from django.shortcuts import render
from courses.models import Course


def index(request):
    cours_table = Course.objects.all()
    return render(request, 'index.html', {'cours_table': cours_table})


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')


