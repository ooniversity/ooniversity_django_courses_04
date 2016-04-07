# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError


def decision(request):
    aknd, bknd, cknd, d, marker, xx = '', '', '', '', '', ''
    try:
        a = int(request.GET['a'])
    except ValueError:
        a = request.GET['a']
        aknd = 'коэффициент не целое число'
    except MultiValueDictKeyError:
        a = ''
        aknd = 'коэффициент не определен'

    try:
        b = int(request.GET['b'])
    except ValueError:
        b = request.GET['b']
        bknd = 'коэффициент не целое число'
    except MultiValueDictKeyError:
        b = None
        bknd = 'коэффициент не определен'

    try:
        c = int(request.GET['c'])
    except ValueError:
        c = request.GET['c']
        cknd = 'коэффициент не целое число'
    except MultiValueDictKeyError:
        c = ''
        cknd = 'коэффициент не определен'

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

    s = {'a': a, 'b': b, 'c': c, 'd': d, 'xx': xx, 'mk': marker, 'aknd': aknd, 'bknd': bknd, 'cknd': cknd}
    return render(request, 'quadratic/results.html', s)
