#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from django.db import models
import math

def quadratic(a, b, c):
    no_err_flag = True
    key_dict = {'a': {'a': a, 'err_mess':'', 'int':''}, 
                'b': {'b': b, 'err_mess':'', 'int':''}, 
                'c': {'c': c, 'err_mess':'', 'int':''}}
    for i in key_dict:
        try:
            key_dict[i]['int'] = float(key_dict[i][i])
        except ValueError:
            if key_dict[i][i]:
                key_dict[i]['err_mess'] = 'коэффициент не целое число'
            else:
                key_dict[i]['err_mess'] = 'коэффициент не определен'
            no_err_flag = False
    if key_dict['a']['int'] == 0:
        key_dict['a']['err_mess'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        no_err_flag = False
    key_dict['r'] = ''
    key_dict['res_mess'] = '' 
    if no_err_flag:
        a = key_dict['a']['int']
        b = key_dict['b']['int']
        c = key_dict['c']['int']
        r = b**2 - 4 * a * c
        key_dict['r'] = 'Дискриминант: %d' % r
        if r == 0:
            x = round((-b) / (2 * a),1)
            key_dict['res_mess'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}'.format(x)
        elif r > 0 :
            x = round(((-b) + math.sqrt(r)) / (2 * a),1)
            y = round(((-b) - math.sqrt(r)) / (2 * a),1)
            key_dict['res_mess'] = 'Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}'.format(x,y)
        if r < 0 :
            key_dict['res_mess'] = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    return key_dict

    tr