# -*- coding: utf-8 -*-
from django.shortcuts import render


def is_valid_arg(arg, first=False):
    try:
        int_arg = int(arg)
        err_mess = ''
        if int_arg == 0 and first:
            err_mess = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    except ValueError:
        if not str(arg):
            int_arg = ''
            err_mess = 'коэффициент не определен'
        elif not str(arg).isdigit():
            int_arg = str(arg)
            err_mess = 'коэффициент не целое число'

    return (int_arg, err_mess)

def quadratic_results(request):
    a = is_valid_arg(request.GET['a'], True)
    b = is_valid_arg(request.GET['b'])
    c = is_valid_arg(request.GET['c'])
    discr = ''
    result_answer = ''
    if not (a[1] or b[1] or c[1]):
        d = b[0]**2 - 4*a[0]*c[0]
        if d > 0:
            x1 = (-b[0] + d**(1/2.0))/(2.0*a[0])
            x2 = (-b[0] - d**(1/2.0))/(2.0*a[0])
            result_answer = 'Квадратное уравнение имеет два действительных корня: x1 = {0}, x2 = {1}'.format(x1, x2)
        elif d == 0:
            x = -b[0]/(2.0*a[0])
            result_answer = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0}'.format(x)
        elif d < 0:
            result_answer = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        discr = 'Дискриминант: {0}'.format(d)

    results_dict = ({'arg': 'a = {0}'.format(a[0]), 'mess': a[1]},
              {'arg': 'b = {0}'.format(b[0]), 'mess': b[1]},
              {'arg': 'c = {0}'.format(c[0]), 'mess': c[1]})

    return render(request, 'quadratic/results.html',{
                  'results_dict': results_dict,
                  'discriminant': discr,
                  'result_answer': result_answer
                  })
