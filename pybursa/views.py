from django.shortcuts import render
from courses.models import Course


def index(request):
    """ основная страница со списком курсов """
    course=Course.objects.all()
    return render(request, 'index.html', {"courses_list":course})

    
def contact(request):
    """ контакты организаторов"""
    return render(request, 'contact.html')
