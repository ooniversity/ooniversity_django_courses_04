from django.shortcuts import render
from models import Student


def list_view(request):
	deskr = Student.objects.all()
	mtm = Student.objects.filter(student__courses)

	return render(request, 'students/list.html', {'deskr':deskr, 'mtm':mtm})