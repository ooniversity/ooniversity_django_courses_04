# -*- coding: utf-8 -*-
from django.shortcuts import render
from forms import QuadraticForm


# Create your views here.
def quadratic_results(request):

    context = {}
    if request.method == 'GET':
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            d = int(b ** 2 - 4 * a * c)
            if d > 0:
                text = "Квадратное уравнение имеет два действительных корня: x1 = %0.1f, x2 = %0.1f" % (get_results(a, b, d), get_results(a, b, d, 2))
            elif d == 0:
                text = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %0.1f" % (get_results(a, b, d))
            else:
                text = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            context['d'] = str(d)
            context['results'] = text
    else:
        form = QuadraticForm()


    context['form'] = form
    return render(request, 'quadratic/results.html', context)


def get_results(a, b, d, order=1):
    if order == 1:
        x = (-b + d**(1/2.0)) / 2*a
    else:
        x = (-b - d**(1/2.0)) / 2*a
    return x