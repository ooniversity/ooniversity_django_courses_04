from django.shortcuts import get_object_or_404, render
from datetime import date
from students.models import Student
from courses.models import Course

def detail(request, student_id):
    student = get_object_or_404(Student, id = int(student_id))
    student_date = student.date_of_birth.strftime("%.4B %d, %Y")
    student_courses_list = Course.objects.filter(id__in[])
    return render(request, 'students/detail.html', {'student':student, 'student_date':student_date})

def list_view(request):
    course_id = int(request.GET['course_id'])
    list_of_students = Student.objects.filter(courses = course_id)
    