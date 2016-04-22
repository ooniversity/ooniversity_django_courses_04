# -*- coding: utf-8 -*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    disc = {}
    text_result = {}
    if request.GET == {}:
        form = QuadraticForm()
    else:
        form = QuadraticForm(request.GET)
        if request.method == "GET":
            if form.is_valid():
                data = form.cleaned_data
                disc['message'] = "Дискриминант: "
                disc['value'] = data['b']**2 - 4*data['a']*data['c']
                if disc['value'] < 0:
                    text_result['message'] = u"Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
                elif disc['value'] == 0:
                    x = (-data['b'] + disc['value'] ** (1/2.0)) / 2*data['a']
                    text_result['message'] = u"Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = "
                    text_result['value'] = x
                else:
                    x1 = (-data['b'] + disc['value'] ** (1/2.0)) / 2*data['a']
                    x2 = (-data['b'] - disc['value'] ** (1/2.0)) / 2*data['a']
                    text_result['message'] = (u"Квадратное уравнение имеет два действительных корня: ")
                    text_result['value'] = u"x1 = %.1f, x2 = %.1f" % (x1, x2)

    context = {"disc": disc, "text_result": text_result, "form": form}

    return render(request, 'quadratic/results.html', context)
