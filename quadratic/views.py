# -*- coding: utf-8 -*-
from django.shortcuts import render

import math


def quadratic_results(request):
    req_data = request.GET

    parsed_data = []

    if req_data:
        a = req_data['a']
        str_a = ""
        if a == "":
            str_a = "коэффициент не определен"
        else:
            try:
                a = int(a)
            except ValueError:
                    a = str(a)
                    str_a = "коэффициент не целое число"
            if a == 0:
                str_a = """коэффициент при первом слагаемом уравнения,
                    не может быть равным нулю"""
        parsed_data.append(a)

        b = (req_data['b'])
        str_b = ""
        if b == "":
            str_b = "коэффициент не определен"
        else:
            try:
                b = int(b)
            except ValueError:
                b = str(b)
                str_b = "коэффициент не целое число"
        parsed_data.append(b)

        c = (req_data['c'])
        str_c = ""
        if c == "":
            str_c = "коэффициент не определен"
        else:
            try:
                c = int(c)
            except ValueError:
                c = str(c)
                str_c = "коэффициент не целое число"
        parsed_data.append(c)

        if type(a) is int and type(b) is int and type(c) is int:
            discr = b**2 - 4 * a * c
            if discr > 0:
                x1 = (-b + math.sqrt(discr)) / (2 * a)
                x2 = (-b - math.sqrt(discr)) / (2 * a)
                discr_title = 'Дискриминант: '
                discr_text = '''Квадратное уравнение имеет два
                действительных корня:'''
                context_data = {
                    'a': a,
                    'b': b,
                    'c': c,
                    'str_a': str_a,
                    'str_b': str_b,
                    'str_c': str_c,
                    'discr': discr,
                    'discr_title': discr_title,
                    'discr_text': discr_text,
                    'x1': x1,
                    'x2': x2
                }
            elif discr < 0:
                discr_title = 'Дискриминант: '
                discr_text = '''Дискриминант меньше нуля, квадратное
                уравнение не имеет действительных решений.'''
                context_data = {
                    'a': a,
                    'b': b,
                    'c': c,
                    'str_a': str_a,
                    'str_b': str_b,
                    'str_c': str_c,
                    'discr': discr,
                    'discr_title': discr_title,
                    'discr_text': discr_text
                }
            elif a == 0:
                context_data = {
                    'a': a,
                    'b': b,
                    'c': c,
                    'str_a': str_a,
                    'str_b': str_b,
                    'str_c': str_c,
                    }
            else:
                x = -b / (2 * a)
                x = float(x)
                discr_title = 'Дискриминант: '
                discr_text = '''Дискриминант равен нулю, квадратное
                уравнение имеет один действительный корень: x1 = x2 = '''
                context_data = {
                    'a': a,
                    'b': b,
                    'c': c,
                    'str_a': str_a,
                    'str_b': str_b,
                    'str_c': str_c,
                    'discr': discr,
                    'discr_title': discr_title,
                    'discr_text': discr_text,
                    'x': x,
                    }
        else:
            context_data = {
                    'a': a,
                    'b': b,
                    'c': c,
                    'str_a': str_a,
                    'str_b': str_b,
                    'str_c': str_c,
                    }

        return render(request, 'quadratic/results.html', context_data)

    else:
        context_data = {'string': "Квадратное уравнение a*x*x + b*x + c = 0",
                        'info': '''Для произведения вычислений,
                        добавьте значения коэффициентов в строку URL
                        в формате: ?a=1&b=3&c=5'''}
        return render(request, 'quadratic/results.html', context_data)
