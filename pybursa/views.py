from django.shortcuts import  render, get_object_or_404


from django.core.urlresolvers import reverse


from django.views import generic


from courses.models import Course


def contact(request):
    print 'Start contact view!'
    return render(request, 'contact.html')


def student_list(request):
    print 'Start student_list view!'
    return render(request, 'student_list.html')


def student_detail(request):
    print 'Start student_detail view!'
    return render(request, 'student_detail.html')


def courses_info(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})