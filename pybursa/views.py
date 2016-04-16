<<<<<<< HEAD
from django.shortcuts import  render

def index(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')

def student_detail(request):
	return render(request, 'student_detail.html')
      
def results(request):
	return render(request, 'results.html')      
=======
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')
>>>>>>> f114d78577c0d563bac959a439787d0446e06ff9
