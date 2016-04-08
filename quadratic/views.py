# -*- coding: utf-8 -*-
import math
from django.template import loader, Context
from django.shortcuts import render

def quadratic_results(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    
    # 'warning_'+'a'
    dic = {'a': a, 'b': b, 'c': c}
    res = {}

    for i in dic:
        
        if dic[i] == '':
            res[i] = 'коэффициент не определен'

        else:
            if not dic[i].isdigit():
                res[i] = 'коэффициент не целое число'
            else:
                if dic['a'] == 0:
                    res['a'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю 1'
                else:
                    res[i] = ''
                    if a == 0:
                        res['a'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
                        x = ''
                        same_root = ''
                        continue
                    else:
                        res['a'] = ''
                        #############
                        
                        if a == '':
                            a = ''
                            res['a'] = 'коэффициент не определен'
                            b = int(b)
                            c = int(c)
                            des = ''
                            des_warn = ''
                            x1 = ''
                            x2 = ''
                            root_mes = ''
                            x = ''
                            same_root = ''
                             ###################

                        else:
                            a = int(a)
                            #a = int(a)
                            b = int(b)
                            c = int(c)
                            des = b**2-4*a*c

                            if des < 0:
                                des_warn = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
                                x1 = ''
                                x2 = ''
                                root_mes = ''
                                x = ''
                                same_root = ''
                            elif des == 0:
                                des_warn = ''
                                x1 = ''
                                x2 = ''
                                root_mes = ''
                                x = (-b+math.sqrt(b**2-4*a*c))/2*a
                                same_root = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 ='
                            else:
                                des_warn = ''
                                root_mes = 'Квадратное уравнение имеет два действительных корня: '
                                x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
                                x2 = (-b-math.sqrt(b**2-4*a*c))/2*a



    return render(request, 'quadratic/results.html', {
        'a': a,
        'b': b, 
        'c': c, 
        'warning_a': res['a'], 
        'warning_b': res['b'], 
        'warning_c': res['c'],
        'des': des,
        'des_warn': des_warn,
        'x1': x1,
        'x2': x2,
        'root_mes': root_mes,
        'x': x,
        'same_root': same_root
        })




