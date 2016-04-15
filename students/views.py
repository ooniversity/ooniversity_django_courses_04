from django.shortcuts import render
from students.models import Student
from courses.models import Course

def list_view(request):	
	if request.GET:
		course_id = request.GET['course_id']
		students = Student.objects.filter(courses=course_id).order_by('id')	
	else:
		students = Student.objects.all()
	
	return render(request, 'students/list_view.html', {'students':students})

def student_detail(request, id):
	student = Student.objects.get(id=id)
	return render(request, 'students/detail.html', {'student':student})
	
