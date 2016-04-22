# -*- coding: utf-8 -*-
from django.shortcuts import render

from quadratic.forms import QuadraticForm

# def valid_arg(arg, first=False):
#     try:
#         int_arg = int(arg)
#         err_mess = ''
#         if int_arg == 0 and first:
#             err_mess = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
#     except ValueError:
#         if not str(arg):
#             int_arg = ''
#             err_mess = 'коэффициент не определен'
#         elif not str(arg).isdigit():
#             int_arg = str(arg)
#             err_mess = 'коэффициент не целое число'

#     return (int_arg, err_mess)

def quadratic_results(request):
    form = QuadraticForm()
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            discr = ''
            result_answer = ''
            d = b**2 - 4*a*c
            if d > 0:
                x1 = (-b + d**(1/2.0))/(2.0*a)
                x2 = (-b - d**(1/2.0))/(2.0*a)
                result_answer = 'Квадратное уравнение имеет два действительных корня: x1 = {0}, x2 = {1}'.format(x1, x2)
            elif d == 0:
                x = -b/(2.0*a)
                result_answer = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0}'.format(x)
            elif d < 0:
                result_answer = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            discr = 'Дискриминант: {0}'.format(d)

            return render(request, 'quadratic/results.html',
                          {'discriminant': discr,
                          'result_answer': result_answer,
                          'form': form})
    return render(request, 'quadratic/results.html', {'form': form})
