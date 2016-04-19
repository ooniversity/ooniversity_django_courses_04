# -*- coding: utf-8 -*-
from django.shortcuts import render
from forms import QuadraticForm


def quadratic_results(request):
    context = {}
    if request.GET:
        form = QuadraticForm(request.GET)
        context['form'] = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            d = b ** 2 - 4 * a * c
            if d < 0:
                context['xx'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            elif d == 0:
                x = -b / 2.0*a
                context['xx'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x
            else:
                x1 = (-b + d ** (1/2.0)) / (2*a)
                x2 = (-b - d ** (1/2.0)) / (2*a)
                context['xx'] = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2)
            context['d'] = 'Дискриминант: %s' %d
    else:
        context['form'] = QuadraticForm()
    return render(request, 'quadratic/results.html', context)

