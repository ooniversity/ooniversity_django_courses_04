# -*- coding: utf-8 -*- 
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

class QT(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_discrim(self):
        self.d = self.b ** 2 - 4 * self.a * self.c

    def get_discrim(self):
         return self.d

    def get_eq_root(self, order=1):
        if order==1:
            x = (-self.b + self.d ** (1/2.0)) / 2*self.a
        else:
            x = (-self.b - self.d ** (1/2.0)) / 2*self.a
        return x


def quadratic_results(request):
    ER = {}

    a = request.GET.__getitem__('a')
    b = request.GET.__getitem__('b')
    c = request.GET.__getitem__('c')

    V = request.GET.dict()
    for var in V:
        if V[var] == "":
            ER[var] = 'коэффициент не определен'
        if V[var].isalpha():
            ER[var] = 'коэффициент не целое число'
        if '.' in V[var]:
            ER[var] = 'коэффициент не целое число'

    if V['a'].isdigit() and int(V['a']) == 0:
        ER['a'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

    if len(ER)==0:
        quad = QT(int(a), int(b), int(c))
        quad.calc_discrim()
        d = quad.get_discrim()
        V.update(d=d)

        if d >= 0:
            x1 = quad.get_eq_root()
            x2 = quad.get_eq_root(order=2)
            V.update(x1=x1, x2=x2)
    
    return render(request, 'results.html', {'var':V, 'errors':ER})


