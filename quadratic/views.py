# -*- coding: utf-8 -*-
from django.shortcuts import render


def quadratic_results(request):
    aknd, bknd, cknd, d, marker, xx = '', '', '', '', '', ''
    try:
        a = int(request.GET['a'])
    except ValueError:
        a = request.GET['a']
        if a == '':
            aknd = 'коэффициент не определен'
        else:
            aknd = 'коэффициент не целое число'

    try:
        b = int(request.GET['b'])
    except ValueError:
        b = request.GET['b']
        if b == '':
            bknd = 'коэффициент не определен'
        else:
            bknd = 'коэффициент не целое число'

    try:
        c = int(request.GET['c'])
    except ValueError:
        c = request.GET['c']
        if c == '':
            cknd = 'коэффициент не определен'
        else:
            cknd = 'коэффициент не целое число'

    if type(a) == int and type(b) == int and type(c) == int:
        d = b ** 2 - 4 * a * c
        if a == 0:
            marker = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        elif d < 0:
            xx = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif d == 0:
            x = -b / 2*a
            xx = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x
        else:
            x1 = (-b + d ** (1/2.0)) / (2*a)
            x2 = (-b - d ** (1/2.0)) / (2*a)
            xx = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2)
        d = 'Дискриминант: %s' %d
    if a == 0:
        d = ''
        marker = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    s = {'a': a, 'b': b, 'c': c, 'd': d, 'xx': xx, 'mk': marker, 'aknd': aknd, 'bknd': bknd, 'cknd': cknd}
    return render(request, 'quadratic/results.html', s)
