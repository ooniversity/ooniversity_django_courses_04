# -*- coding: utf-8 -*-
from django.shortcuts import render


def quadratic_results(request):
    dict_param = request.GET.dict()
    warning = {}
    for param in dict_param.items():
        if bool(param[1]):
            pass
        else:
            warning[param[0]] = 'коэффициент не определен'
            continue
        if param[1].isdigit() and type(param[1] is not float):
            pass
        else:
            warning[param[0]] = 'коэффициент не целое число'
            continue
        if param[0] == 'a' and int(param[1]) == False:
            warning[param[0]] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        else:
            continue

    d = int(dict_param['b'])**2 - 4*int(dict_param['a'])*int(dict_param['c'])

    if d > 0:
        x1 = (-int(dict_param['b']) + d**(1.0/2)) / 2 * int(dict_param['a'])
        x2 = (-int(dict_param['b']) - d**(1.0/2)) / 2 * int(dict_param['a'])
        info = 'Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}'.format(x1, x2)
    elif d == 0:
        x1 = x2 = (-int(dict_param['b']) + d**(1.0/2)) / 2 * int(dict_param['a'])
        info = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}'.format(x1)
    elif d < 0:
        info = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'

    return render(request, 'results.html', locals())
