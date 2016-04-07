# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError


def decision(request):
    d = ''
    xx = ''
    marker = ''
    aknd = ''
    akng = ''
    bknd = ''
    bkng = ''
    cknd = ''
    ckng = ''
    try:
        a = request.GET['a']
    except MultiValueDictKeyError:
        a = ''

    try:
        b = request.GET['b']
    except MultiValueDictKeyError:
        b = ''

    try:
        c = request.GET['c']
    except MultiValueDictKeyError:
        c = ''

    try:
        a = int(a)
        b = int(b)
        c = int(c)
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
    except:
        if a == '':
            aknd = 'коэффициент не определен'
        else:
            akng = 'коэффициент не целое число'
        if b == '':
            bknd = 'коэффициент не определен'
        else:
            bkng = 'коэффициент не целое число'
        if c == '':
            cknd = 'коэффициент не определен'
        else:
            ckng = 'коэффициент не целое число'
    s = {'a': a, 'b': b, 'c': c, 'd': d, 'xx': xx, 'mk': marker, 'aknd': aknd, 'akng': akng, 'bknd': bknd, 'bkng': bkng, 'cknd': cknd, 'ckng': ckng}
    return render(request, 'quadratic/results.html', s)
