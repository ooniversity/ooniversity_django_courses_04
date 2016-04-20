from django.shortcuts import render, redirect
from students.models import Student
from forms import StudentModelForm
from django.contrib import messages


def list_view(request):
	if request.GET:
		deskr = Student.objects.filter(courses__id=int(request.GET['course_id']))
	else:
		deskr = Student.objects.all()
	return render(request, 'students/list.html', {'deskr':deskr})


def detail(request, student_id):
	det = Student.objects.get(id=student_id)
	return render(request, 'students/detail.html', {'det':det})

def create(request):
	if request.method == 'POST':
		model = StudentModelForm(request.POST)
		if model.is_valid():
			form = model.save()
			messages.success(request, 'Student')
			return redirect('students:list_view')
	else:
		model = StudentModelForm()
	return render(request, 'students/add.html', {'model':model})

def edit(request, student_id):
	form = Student.objects.get(id=student_id)
	model = StudentModelForm(instance=form)
	return render(request, 'students/edit.html', {'form':form})