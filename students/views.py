from django.shortcuts import render
from django.http import HttpResponse

def list_view(request):
	return render (request, 'students/list.html')
def detail(request):
	return render (request, 'students/detail.html')