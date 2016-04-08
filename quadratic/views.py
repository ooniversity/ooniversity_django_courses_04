# -*- coding: utf-8 -*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm
from django import forms



class Validation(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.value_int = None
        self.error_msg = None

    def valid_quadratic(self):
        if not self.value:
            self.error_msg = 'коэффициент не определен'
            return False
        try:
            self.value_int = int(self.value)
        except ValueError:
            self.error_msg = 'коэффициент не целое число'
            return False

        if self.name == 'a' and self.value_int == 0:
            self.error_msg = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
            return False
        return True


def quadratic_results(request):
    """
    discriminant check
    calculation of the square root of the equation
    """
    context = {'error': False}
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
        else:
            form = QuadraticForm()
            context.update({ 'form' : form })

    for name_value in ['a', 'b', 'c']:
        valid = Validation(name_value, request.GET.get(name_value, ''))
        if valid.valid_quadratic():
            context[name_value] = valid.value_int
        else:
            context['error'] = True
            context[name_value + '_error'] = valid.error_msg
            context[name_value] = valid.value
    if not context['error']:
        a = context['a']
        b = context['b']
        c = context['c']
        d = b ** 2 - 4 * a * c

        if d < 0:
            result = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        elif d == 0:
            x1 = x2 = (-b + d ** (1/2.0))/ (2 * a)
            result = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %0.1f" % (x1)
        else:
            x1 = (-b + d ** (1/2.0)) / (2 * a)
            x2 = (-b - d ** (1/2.0)) / (2 * a)
            result = "Квадратное уравнение имеет два действительных корня: x1 = %0.1f, x2 = %0.1f" % (x1, x2)
        context.update({'d': str(int(d)), 'result': str(result)})


        #context.update({'form': form})
    return render(request, "results.html", context)

