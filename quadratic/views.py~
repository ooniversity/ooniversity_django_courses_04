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
        er_a = u'коэффициент не целое число'
    try:
        b = int(request.GET['b'])
    except ValueError:
        b = request.GET['b']
        er_b = u'коэффициент не целое число'
    try:
        c = int(request.GET['c'])
    except ValueError:
        c = request.GET['c']
        er_c = u'коэффициент не целое число'

    d = None

    if a == 0:
        er_a = u'коэффициент при первом слагаемом уравнения не может быть равным нулю'

    if not a and a != 0:
        er_a = u'коэффициент не определен'

    if not b and b !=0:
        er_b = u'коэффициент не определен'

    if  not c and c !=0:
        er_c = u'коэффициент не определен'

    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int) and a != 0:
        d = discr(a, b, c)

    if d and d < 0:
        er_d = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    if d == 0:
        x = korni(d, a, b)
        er_d = u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %0.1f' % x
    if d and d > 0:
        x = korni(d, a, b)
        er_d =  u'Квадратное уравнение имеет два действительных корня: x1 = %0.1f, x2 = %0.1f' % (float(x[0]), float(x[1]))
        d = int(d)


    return render(request, 'results.html', {'a': a, 'b':b, 'c': c, 'er_a': er_a, 'er_b': er_b, 'er_c': er_c, 'd':d, 'st_d': er_d})

def discr(a, b, c):
    return (b*b-4*a*c)

def korni(d, a, b):
    if d == 0:
        return (-b/2*a)
    else:
        d = d**(1/2.0)
        return [(-b+d)/2*a, (-b-d)/2*a]