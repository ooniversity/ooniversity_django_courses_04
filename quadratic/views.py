# -*- coding: utf8 -*-
from django.shortcuts import render


def quadratic_results(request):
    return render(request, 'results.html', get_coefficients(request))

def get_coefficients(request):
    result_a = result_b = result_c = result_discr = result_message = ''
    coeff_a = coeff_b = coeff_c = 0
    try:
        coeff_a = int(request.GET['a'])
    except ValueError:
        if not request.GET['a'].isdigit():
            if request.GET['a'] != '':
                coeff_a = request.GET['a']
                result_a = u'коэффициент не целое число'
            else:
                result_a = u'коэффициент не определен'

    try:
        coeff_b = int(request.GET['b'])
    except ValueError:
        if not request.GET['b'].isdigit():
            if request.GET['b'] != '':
                coeff_b = request.GET['b']
                result_b = u'коэффициент не целое число'
            else:
                result_b = u'коэффициент не определен'
    try:
        coeff_c = int(request.GET['c'])
    except ValueError:
        if not request.GET['c'].isdigit():
            if request.GET['c'] != '':
                coeff_c = request.GET['c']
                result_c = u'коэффициент не целое число'
            else:
                result_c = u'коэффициент не определен'

    if result_a == result_b == result_c == '':
        if coeff_a == 0:
            result_a = u'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        else:
            discr = coeff_b ** 2 - 4 * coeff_a * coeff_c
            if discr > 0:
                result_discr = u'Дискриминант: %d' % discr
                x1 = (-coeff_b + discr ** (1 / 2.0)) / (2 * coeff_a)
                x2 = (-coeff_b - discr ** (1 / 2.0)) / (2 * coeff_a)
                result_message = u'Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f' % (x1, x2)
            elif discr < 0:
                result_discr = u'Дискриминант: %d' % discr
                result_message = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            else:
                result_discr = u'Дискриминант: %d' % discr
                x = -coeff_b / 2 * coeff_a
                result_message = u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' % x

    return {
                      'coeff_a': coeff_a,
                      'coeff_b': coeff_b,
                      'coeff_c': coeff_c,
                      'result_a': result_a,
                      'result_b': result_b,
                      'result_c': result_c,
                      'result_discr': result_discr,
                      'result_message': result_message
           }
