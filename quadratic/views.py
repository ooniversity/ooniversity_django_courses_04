# -*- coding: UTF-8 -*-
from django.shortcuts import render
from forms import QuadraticForm


def quadratic_results(request):
    context = {}
    context['error'] = True
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            context['error'] = False
            a = form.cleaned_data.get('a')
            b = form.cleaned_data.get('b')
            c = form.cleaned_data.get('c')
            d = b**2 - 4*a*c
            if d < 0:
                result_message = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif d == 0:
                x = (-b + d**(1/2.0)) / 2*a
                result_message = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}.".format(x)
            else:
                x1 = (-b + d**(1/2.0)) / 2*a
                x2 = (-b - d**(1/2.0)) / 2*a
                result_message = "Дискриминант равен нулю, квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}.".format(x1, x2)
            context.update({'d':d, 'result_message': result_message})
        else:
            context['error'] = True
    else:
        form = QuadraticForm()

    context['form'] = form
    return render(request, 'quadratic/results.html', context)

