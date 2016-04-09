# -*- coding: utf-8 -*-
from django.shortcuts import render

def quadratic_results(request):
	try:
		a = int(request.GET['a'])
	except :
		a = request.GET['a']

	try:
		b = int(request.GET['b'])
	except :
		b = request.GET['b']

	try:
		c = int(request.GET['c'])
	except :
		c = request.GET['c']
	d = None	

	data = {'a':a, 'b':b, 'c':c}

	error_a = ""
	error_b = ""
	error_c = ""
	errors = {'a':error_a, 'b':error_b, 'c':error_c}

	need_answer = True
	for key in data:
		if data[key] == '':
			errors[key] = u'коэффициент не определен'
			need_answer = False
			continue
		if not isinstance( data[key], ( int, long ) ):
			errors[key] = u'коэффициент не целое число'	 	
		
		
		if a == 0:
		    errors['a'] = u'коэффициент при первом слагаемом уравнения не может быть равным нулю'
		    need_answer = False
	answer = ""
	if need_answer:
		d = (b ** 2 - 4 * a * c)

		if d < 0:
			answer = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
		elif d == 0:
		    x = float(-b / 2 * a)	
		    answer = u"""Дискриминант равен нулю,
		              квадратное уравнение имеет один 
		              действительный корень: 
		              x1 = x2 = %.1f""" % x
		else:
		    x1 = float((-b + d ** (1/2.0)) / (2*a))              
		    x2 = float((-b - d ** (1/2.0)) / (2*a))  
		    answer = u"""Квадратное уравнение имеет два 
		              действительных корня: 
		              x1 = %.1f, x2 = %.1f""" % (x1, x2)


	return render(request, 'quadratic/results.html', {
	        'data': data, 
	        'errors': errors,
	        'need_answer': need_answer,
	        'answer': answer,
	        'd':d,
	    })
