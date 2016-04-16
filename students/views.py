from django.shortcuts import render

from students.models import Student


def list_view(request):
    students_list = []

    if request.GET and request.GET['course_id']:
        course_id = request.GET['course_id']
        students_set = Student.objects.filter(courses=course_id)
    else:
        students_set = Student.objects.all()

    for student in students_set:
        student_detail = {
            'id':        student.id,
            'full_name': student.surname + ' ' + student.name,
            'address':   student.address,
            'skype':     student.skype,
            'courses':   student.courses.all(),
        }
        students_list.append(student_detail)

    return render(request, 'students/list.html', {'students_list': students_list})


def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    student_courses = student.courses.all()
    parameters = {
        'student': student,
        'courses': student_courses,
    }
    return render(request, 'students/detail.html', parameters)
