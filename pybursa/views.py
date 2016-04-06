from django.shortcuts import render


def main_page (request):
	return render(request, 'index.html')

def contact (request):
	return render(request, 'contact.html')

def studlist (request):
	return render(request, 'student_list.html')

def studdetail (request):
	return render(request, 'student_detail.html')
