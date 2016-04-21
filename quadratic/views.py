#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from django.shortcuts import render
from quadratic.forms import QuadraticForm
import math

def quadratic(abc):
    result = {}
    a = abc['a']
    b = abc['b']
    c = abc['c']
    r = b**2 - 4 * a * c
    result['r'] = 'Дискриминант: %d' % r
    if r == 0:
        x = round((-b) / (2 * a),1)
        result['res_mess'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}'.format(x)
    elif r > 0 :
        x = round(((-b) + math.sqrt(r)) / (2 * a),1)
        y = round(((-b) - math.sqrt(r)) / (2 * a),1)
        result['res_mess'] = 'Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}'.format(x,y)
    if r < 0 :
        result['res_mess'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    return result

def quadratic_results(request):
    if request.GET:
        form = QuadraticForm(request.GET)
        result = {'form': form}
        if form.is_valid():
            abc = form.cleaned_data
            result.update(quadratic(abc))
    else:
        result = {'form': QuadraticForm()}
    return render(request,'results.html', result)

