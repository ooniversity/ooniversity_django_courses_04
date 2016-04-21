# encoding: utf-8
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from forms import QuadraticForm

def quadratic_results(request):
    """ --> request
        return render http obj with results and errors
    """
    context = {}
    context['error'] = True
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            context['error'] = False

            a = form.clean_a()
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            d = b**2 - 4*a*c
            if d < 0:
                res_message = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif d == 0:
                x = (-b + d**(1/2.0)) / 2*a
                res_message = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0}".format(x)
            else:
                x1 = (-b + d**(1/2.0)) / 2*a
                x2 = (-b - d**(1/2.0)) / 2*a
                res_message = "Дискриминант равен нулю, квадратное уравнение имеет два действительных корня: x1 = {0}, x2 = {1}".format(x1, x2)
            context.update({'d':d, 'res_message': res_message})
        else:
            context['error'] = True
    else:
        form = QuadraticForm()

    context['form'] = form
    return render(request, 'quadratic/results.html', context)
