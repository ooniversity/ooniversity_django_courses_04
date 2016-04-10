 # -*- coding: utf-8 -*-
from django.shortcuts import render
#from django.utils.datastructures import MultiValueDictKeyError


def quadratic_results(request):
    
    print('enter viev function')
    #q_dic=request.GET.copy()
    # for lots of params can be "for" threw querry dictionary and copy to my mutable usual dict.
    error_a = ''
    error_b = ''
    error_c = ''
    disc=dict()
    text_result=dict()
    #enter and validate params
    a=request.GET.get(u'a', '')
    if a=='':
    	error_a =u"коэффициент не определен"   
    else:
        try:
            a = int(a)
        except ValueError:
            error_a  = u"коэффициент не целое число"
            
    
    b=request.GET.get(u'b',  '')
    if b=='':
        error_b =u"коэффициент не определен"
    else:
        try:
            b = int(b)
        except ValueError:
            error_b = u"коэффициент не целое число"

    c=request.GET.get(u'c',  '')
    if c=='':
        error_c=u"коэффициент не определен"
    else:
        try:
            c = int(c)
        except ValueError:
            error_c = u"коэффициент не целое число"
    #debug print
    print 'a: ', a, 'b: ', b, 'c: ', c
    print 'a: ', error_a, 'b: ', error_b, 'c: ', error_c

    #------logic--------------------
    if a == 0:
        error_a = u"коэффициент при первом слагаемом уравнения не может быть равным нулю"

    if error_a+error_b+error_c=='' :
        disc['message'] = "Дискриминант: "
        disc['value'] = b**2 - 4*a*c
        print 'disc', disc['value']

        if disc['value'] < 0:
            text_result['message'] = u"Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        
        elif disc['value'] == 0:
            x = (-b + disc['value'] ** (1/2.0)) / 2*a
            text_result['message'] = u"Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = "
            text_result['value'] = x
        
        else:
            x1 = (-b + disc['value'] ** (1/2.0)) / 2*a
            x2 = (-b - disc['value'] ** (1/2.0)) / 2*a
            text_result['message'] = u"Квадратное уравнение имеет два действительных корня: "
            text_result['value'] = u"x1 = %.1f, x2 = %.1f" % (x1, x2)

    response_text = {"error_a": error_a, "error_b": error_b, "error_c": error_c, "disc": disc, "text_result":text_result, 'a':{'message':'a = ','value': a}, 'b':{'message':'b = ', 'value':b}, 'c':{'message':'c = ', 'value':c}}
    
    return render(request, 'results.html', response_text)
 