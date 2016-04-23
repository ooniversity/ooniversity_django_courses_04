# -*- coding: utf-8 -*-
from django.shortcuts import render

from quadratic.forms import QuadraticForm


class Equation(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.d = self.b ** 2 - 4 * self.a * self.c

    def get_discriminant(self):
        return self.d

    def get_eq_root(self, order=1):
        if order == 1:
            x = (-self.b + self.d ** (1/2.0)) / 2 * self.a
        else:
            x = (-self.b - self.d ** (1/2.0)) / 2 * self.a
        return x


def quadratic_results(request):
    parameters = {}
    error = True
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            error = False
            a = form.cleaned_data.get('a')
            b = form.cleaned_data.get('b')
            c = form.cleaned_data.get('c')
            d = b ** 2 - 4 * a * c
            if d < 0:
                result_message = u"Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif d == 0:
                x = (-b + d ** (1 / 2.0)) / 2.0 * a
                result_message = u"Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}.".format(x)
            else:
                x1 = (-b + d ** (1 / 2.0)) / 2.0 * a
                x2 = (-b - d ** (1 / 2.0)) / 2.0 * a
                result_message = u"Дискриминант равен нулю, квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}.".format(x1, x2)
            parameters.update({'d': d, 'result_message': result_message})
        else:
            error = True
    else:
        form = QuadraticForm()

    parameters['error'] = error
    parameters['form'] = form
    return render(request, 'quadratic/results.html', parameters)


def quadratic_results_form(request):
    form = QuadraticForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data

    parameters = {
        'form': form,
    }
    return render(request, 'quadratic/results.html', parameters)
