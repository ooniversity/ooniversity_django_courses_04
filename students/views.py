from django.shortcuts import render
from students.models import Student


def student_list_view(request):
    if request.GET.get('course_id') is None:
        student = Student.objects.all()
        return render(request, 'students/list.html', {'students': student})
    else:
        student = Student.objects.filter(courses__id=request.GET.get('course_id'))
        return render(request, 'students/list.html', {'students': student})


def student_detail_view(request, student_id):
        student = Student.objects.get(id=student_id)
        return render(request, 'students/detail.html', {'students': student})
