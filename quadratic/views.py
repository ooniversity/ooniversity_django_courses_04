# encoding: utf-8
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse

def get_parameter(request,params):
    """ --> str var params_name
        return [{str var_name}{int value, str er_types}]
    """
    args=[]
    for p in params:
        try:
            inp_request = request.GET[p]

            if inp_request and '.' in inp_request and len(inp_request)>0:
                e = u"коэффициент не целое число"
                value = inp_request
            elif not inp_request:

                value = ''
                e = u"коэффициент не определен"
            elif '-' in inp_request or inp_request.isdigit():

                if p == 'a' and inp_request =='0':
                    e=u'коэффициент при первом слагаемом уравнения не может быть равным нулю'
                    value = int(inp_request)
                else:
                    e=''
                    value = int(inp_request)
            else:
                e = u"коэффициент не целое число"
                value = inp_request

        except MultiValueDictKeyError:
            e = u"коэффициент не определен"
            value = ''
        finally:
            args.append([{'var_name':p},{'value':value,'er_type':e}])
    return args

def get_discr(a,b,c):
    """ return discr for eq"""
    d = b**2 - 4*a*c
    return d

def quadratic_results(request):
    """ --> request
        return render http obj with results and errors
    """

    args_mess = get_parameter(request,['a','b','c'])
    a, b, c = args_mess[0][1]['value'], args_mess[1][1]['value'], args_mess[2][1]['value']

    args_errors = [args[1]["er_type"] for args in args_mess]
    errors_in_args = True in [bool(i) for i in args_errors] or a == 0
    correct_args = [bool(i) for i in (a, b, c) if i != ""]


    result=[None,None]

    if not errors_in_args and False not in correct_args:# если нет ошибок с аргументами
        d = get_discr(a, b, c)
        result[0] = d

        if d < 0:
            result[1] = u"Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        elif d == 0:
            x = float(-b / 2*a)
            result[1] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0}".format(x)
        else:
            x1 = (-b + d**(1/2.0)) / (2*a)
            x2 = (-b - d**(1/2.0)) / (2*a)
            result[1] = u"Квадратное уравнение имеет два действительных корня: x1 = {0}, x2 = {1}".format(x1,x2)

    return render(request,'quadratic/results.html', {'args': args_mess,
     "result": result,
      "errors_in_args": errors_in_args})
