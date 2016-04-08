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
    war_a = '' 
    war_b = ''
    war_c = ''       
    x = ''
    same_root = '' 
    des = ''
    des_warn = ''
    x1 = ''
    x2 = ''
    root_mes = ''
    x = ''
    same_root = '' 
    
    if a == '':
        a = ''
        war_a = 'коэффициент не определен'     
    

    elif a == '0':
        war_a = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'    
                
    elif not a.isdigit():
        war_a = 'коэффициент не целое число'
    
    if b == '':
        b = ''
        war_b = 'коэффициент не определен'
    
    elif not b.isdigit():
        war_b = 'коэффициент не целое число'

    if c == '':
        c = ''
        war_c = 'коэффициент не определен'

    elif not c.isdigit():
        war_c = 'коэффициент не целое число'

    else:
        a = int(a)
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
        'warning_a': war_a, 
        'warning_b': war_b, 
        'warning_c': war_c,
        'des': des,
        'des_warn': des_warn,
        'x1': x1,
        'x2': x2,
        'root_mes': root_mes,
        'x': x,
        'same_root': same_root
        })




