from django.shortcuts import render
from django.http import HttpResponse

def detail(request):
	return render (request, 'courses/detail.html')