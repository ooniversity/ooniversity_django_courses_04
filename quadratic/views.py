# encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from forms import QuadraticForm
import math


def quadratic_results(request):
    """ расчет корней квадратного уравнения """
    koef=[0]*3
    koef_names=('a','b','c')
    discr1=x1=x2=''
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():            
            for i in range(0,3):
                koef[i]=int(form.cleaned_data.get(koef_names[i]))
            a,b,c = koef
            discr1= b ** 2 - 4 * a * c
            if discr1 > 0:
                x1 = (-b + math.sqrt(discr1)) / (2.0 * a)
                x2 = (-b - math.sqrt(discr1)) / (2.0 * a)
            elif discr1 == 0:
                x1 = -b / (2.0 * a)
                x2=x1;
    else:
        form = QuadraticForm()
    return render(request,'quadratic/results.html',{'form':form, 'd':discr1, 'x1':x1, 'x2':x2}) 

 


