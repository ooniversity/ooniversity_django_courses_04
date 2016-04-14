# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from students.models import Student
from courses.models import Course

#def list_view(request):

#	s = {
#         'title': "СПИСОК СТУДЕНТОВ"
#        }

#	return render(request, 'students/list.html', s)

def list_view(request):
    if request.GET:
        course_id = int(request.GET['course_id'])
        course = get_object_or_404(Course, id=course_id)
        students_list = course.student_set.all()
        students_list.order_by('id')
    else:
        students_list = Student.objects.all()
        students_list.order_by('id')

    student_courses = dict()

    for st in students_list:
        student_courses[st.id] = st.courses.all()
        s = {
             'students_list': students_list, 
             'course_list': student_courses
             }
    return render(request, 'students/list.html', s)


def detail(request, student_id):
    student = get_object_or_404(Student, id=int(student_id))
    student_courses_list = student.courses.all()
    s = {
         'student':student, 
         'students_courses':student_courses_list
        }
    return render(request, 'students/detail.html', s)
