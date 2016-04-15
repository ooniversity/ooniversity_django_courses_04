from django.shortcuts import render
from students.models import Student


def list_view(request):
	if request.GET:
		deskr = Student.objects.filter(courses__id=int(request.GET['course_id']))
	else:
		deskr = Student.objects.all()
	return render(request, 'students/list.html', {'deskr':deskr})


def detail(request, student_id):
	det = Student.objects.get(id=student_id)
	return render(request, 'students/detail.html', {'det':det})