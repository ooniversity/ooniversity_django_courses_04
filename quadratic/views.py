# -- coding: utf-8 --
from django.shortcuts import render

def quadratic_results(request, a=None, b=None, c=None):
    er_a = ''
    er_b = ''
    er_c = ''
    er_d = ''
    q = request.GET
    d = None

    if q['a'].isdigit():
        if int(q['a']) == 0:
            er_a = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    else:
        er_a = 'коэффициент не целое число'
    if not q['a']:
        er_a = 'коэффициент не определен'

    if not q['b'].isdigit():
        er_b = 'коэффициент не целое число'
    if not q['b']:
        er_b = 'коэффициент не определен'

    if not q['c'].isdigit():
        er_c = 'коэффициент не целое число'
    if not q['c']:
        er_c = 'коэффициент не определен'

    if q['c'].isdigit() and q['b'].isdigit() and q['a'].isdigit() and int(q['a']) != 0:
        round(d) = discr(int(q['a']), int(q['b']), int(q['c']))


    if d and d < 0:
        er_d = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    if d and d == 0:
        x = korni(d, int(q['a']), int(q['b']))
        er_d = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x
    if d and d > 0:
        x = korni(d, int(q['a']), int(q['b']))
        er_d = 'Квадратное уравнение имеет два действительных корня: x1 = %d, x2 = %d' % (x[0], x[1])

    return render(request, 'results.html', {'a': q['a'], 'b':q['b'], 'c': q['c'], 'er_a': er_a, 'er_b': er_b, 'er_c': er_c, 'd':d, 'st_d': er_d})

def discr(a,b,c):
    return (b*b-4*a*c)^(1/2)

def korni(d, a, b):
    if d == 0:
        return -b/2*a
    else:
        return [(-b+d)/2*a, (-b-d)/2*a]