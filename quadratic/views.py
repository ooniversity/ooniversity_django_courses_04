# -*- coding: utf-8 -*-
from django.shortcuts import render


def quadratic_results(request):
    req_data = request.GET

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
            a = """коэффициент при первом слагаемом уравнения,
                не может быть равным нулю"""

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

    return render(request, 'results.html', {'a': a,
                                            'b': b,
                                            'c': c,
                                            'str_a': str_a,
                                            'str_b': str_b,
                                            'str_c': str_c
                                            })
