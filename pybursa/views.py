from django.shortcuts import render

from courses.models import Course


def index(request):
    # courses = (
    #     {'id': 1, 'name': 'Course name 1', 'short_description': 'Course Description 1'},
    #     {'id': 2, 'name': 'Course name 2', 'short_description': 'Course Description 2'},
    #     {'id': 3, 'name': 'Course name 3', 'short_description': 'Course Description 3'},
    # )
    courses = Course.objects.only('id', 'name', 'short_description')
    parameters = {
        'courses': courses,
    }
    return render(request, 'index.html', parameters)


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')
