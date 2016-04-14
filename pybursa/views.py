from django.shortcuts import render


def index(request):
    parameters = {
        'courses': (
            {'id': 1, 'name': 'Course name 1', 'description': 'Course Description 1'},
            {'id': 2, 'name': 'Course name 2', 'description': 'Course Description 2'},
            {'id': 3, 'name': 'Course name 3', 'description': 'Course Description 3'},
        ),
    }
    return render(request, 'index.html', parameters)


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')
