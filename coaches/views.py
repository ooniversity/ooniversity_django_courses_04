from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def detail(request):
	return render (request, 'coaches/detail.html')