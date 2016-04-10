from django.shortcuts import render
from quadratic.models import quadratic

def quadratic_results(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return render(request,'results.html', quadratic(a, b, c))

