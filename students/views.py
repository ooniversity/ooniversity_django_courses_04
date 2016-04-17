from django.shortcuts import get_object_or_404, render
from datetime import date
from students.models import Student
from courses.models import Course

def detail(request, student_id):
    student = get_object_or_404(Student, id=int(student_id))
    student_courses_list = student.courses.all()
    return render(request, 'students/detail.html', {'student':student, 'students_courses':student_courses_list})

def list_view(request):
    if request.GET:
        course_id = int(request.GET['course_id'])
        course = get_object_or_404(Course, id=course_id)
        list_of_students = course.student_set.all()
        list_of_students.order_by('id')
    else:
        list_of_students = Student.objects.all()
        list_of_students.order_by('id')

    student_courses = dict()
    for stud in list_of_students:
        student_courses[stud.id] = stud.courses.all()
    return render(request, 'students/list.html', {'students_list': list_of_students, 'course_list': student_courses})