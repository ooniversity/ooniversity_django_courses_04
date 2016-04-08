# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError


def quadratic_results(request):
    a = ''
    b = ''
    c = ''
    error_a = ''
    error_b = ''
    error_c = ''
    disc = {}
    text_result = {}

    try:
        a = int(request.GET['a'])
    except ValueError:
        if request.GET['a'].isalpha():
            error_a = u"коэффициент не целое число"
            a = request.GET['a']
        else:
            error_a = u"коэффициент не определен"
    except MultiValueDictKeyError:
            a = ''
            error_a = u"коэффициент не определен"

    try:
        b = int(request.GET['b'])
    except ValueError:
        if request.GET['b'].isalpha():
            error_b = u"коэффициент не целое число"
            b = request.GET['b']
        else:
            error_b = u"коэффициент не определен"
    except MultiValueDictKeyError:
            b = ''
            error_b = u"коэффициент не определен"

    try:
        c = int(request.GET['c'])
    except ValueError:
        if request.GET['c'].isalpha():
            error_c = u"коэффициент не целое число"
            c = request.GET['c']
        else:
            error_c = u"коэффициент не определен"
    except MultiValueDictKeyError:
        c = ''
        error_c = u"коэффициент не определен"

    if a == 0:
        error_a = u"коэффициент при первом слагаемом уравнения не может быть равным нулю"

    if not error_a and not error_b and not error_c :
        disc['message'] = "Дискриминант: "
        disc['value'] = b**2 - 4*a*c

        if disc['value'] < 0:
            text_result['message'] = u"Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        elif disc['value'] == 0:
            x = (-b + disc['value'] ** (1/2.0)) / 2*a
            text_result['message'] = u"Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = "
            text_result['value'] = x
        else:
            x1 = (-b + disc['value'] ** (1/2.0)) / 2*a
            x2 = (-b - disc['value'] ** (1/2.0)) / 2*a
            text_result['message'] = u"Квадратное уравнение имеет два действительных корня: "
            text_result['value'] = u"x1 = %.1f, x2 = %.1f" % (x1, x2)


    content = {"error_a":error_a, "error_b":error_b, "error_c":error_c, "disc":disc, "text_result":text_result, 'a':{'message':'a = ','value': a}, 'b':{'message':'b = ', 'value':b}, 'c':{'message':'c = ', 'value':c}}

    return render(request, 'results.html', content)

