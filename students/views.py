from django.shortcuts import render
from models import Student


def list_view(request):
	if request.GET:
		deskr = Student.objects.filter(courses__id=int(request.GET['course_id']))
	else:
		deskr = Student.objects.all()
		
	return render(request, 'students/list.html', {'deskr':deskr})

def detail(request):
	return render(request, 'students/detail')