from django.shortcuts import render
from courses.models import Course
from students.models import Student

def list_view(request):
	course_id = request.GET.get('course_id')

	if course_id:
		students = Student.objects.filter(courses__id=course_id)
	else:
		students = Student.objects.all()	
	return render(request, 'students/list_view.html', locals())

def detail(request, student_id):
	student = Student.objects.get(id=student_id)
	student_courses = student.courses.all()
	return render(request, 'students/detail.html', locals())


