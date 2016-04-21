#-*- coding: utf-8 -*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm

def get_discr(a, b, c):
    d = b ** 2 - 4 * a * c
    return d


def get_root(a, b, d, order=1):
    if order == 1:
        x = (-b + d ** (1/2.0)) / (2*a)
    else:
        x = (-b - d ** (1/2.0)) / (2*a)
    return x

def quadratic_results(request):
    form = QuadraticForm()
    context = {}
    if request.method == 'GET':
        form = QuadraticForm(request.GET)
        if form.is_valid():
            data=form.cleaned_data
            d = get_discr(**data)
            if d < 0:
                result_message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            elif d==0:
                x = get_root(data['a'], data['b'], d)
                result_message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' %x
            else:
                x1 = get_root(data['a'], data['b'], d)
                x2 = get_root(data['a'], data['b'], d, order=2)
                result_message = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' %(x1, x2)
            context.update({'d':d, 'result_message':result_message})
    else:
        form = QuadraticForm()
    context.update({'form':form})        
    return render (request, 'results.html', context)
