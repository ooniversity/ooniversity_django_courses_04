# -- coding: utf-8 --
from django.shortcuts import render

def quadratic_results(request, a=None, b=None, c=None):
    er_a = ''
    er_b = ''
    er_c = ''
    er_d = ''

    try:
        a = int(request.GET['a'])
    except ValueError:
        a = request.GET['a']
        er_a = 'коэффициент не целое число'
    try:
        b = int(request.GET['b'])
    except ValueError:
        b = request.GET['b']
        er_b = 'коэффициент не целое число'
    try:
        c = int(request.GET['c'])
    except ValueError:
        c = request.GET['c']
        er_c = 'коэффициент не целое число'

    d = None

    if a == 0:
        er_a = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

    if not a and a !=0:
        er_a = 'коэффициент не определен'

    if not b:
        er_b = 'коэффициент не определен'

    if  not c:
        er_c = 'коэффициент не определен'

    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int) and a != 0:
        d = discr(a, b, c)

    if d and d < 0:
        er_d = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    if d and d == 0:
        x = korni(d, a, b)
        er_d = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x
    if d and d > 0:
        x = korni(d, a, b)
        er_d = 'Квадратное уравнение имеет два действительных корня: x1 = %d, x2 = %d' % (x[0], x[1])

    return render(request, 'results.html', {'a': a, 'b':b, 'c': c, 'er_a': er_a, 'er_b': er_b, 'er_c': er_c, 'd':d, 'st_d': er_d})

def discr(a, b, c):
    return (b*b-4*a*c)^(1/2)

def korni(d, a, b):
    if d == 0:
        return -b/2*a
    else:
        return [(-b+d)/2*a, (-b-d)/2*a]