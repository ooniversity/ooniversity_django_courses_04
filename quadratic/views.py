# -*- coding: utf-8 -*-
from django.shortcuts import render

def quadratic_results(request):
	param_a = str()
	param_b = str()
	param_c = str()
	disc = {}
	result = {}

	try:
		a = int(request.GET['a'])
	except ValueError:
		if request.GET['a'].isalpha():
			param_a = "коэффициент не целое число"
			a = request.GET['a']
		else:
			param_a = "коэффициент не определен"

	try:
		b = int(request.GET['b'])
	except ValueError:
		if request.GET['b'].isalpha():
			param_b = "коэффициент не целое число"
			b = request.GET['b']
		else:
			param_b = "коэффициент не определен"

	try:
		c = int(request.GET['c'])
	except ValueError:
		if request.GET['c'].isalpha():
			param_c = "коэффициент не целое число"
			c = request.GET['c']
		else:
			param_c = "коэффициент не определен"

	if 'a' in locals():
		if a == 0:
			param_a = "коэффициент при первом слагаемом уравнения не может быть равным нулю"

	if not param_a and not param_b and not param_c :
		disc['message'] = "Дискриминант: "
		disc['value'] = b**2 - 4*a*c

		if disc['value'] < 0:
			result['message'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
		elif disc['value'] == 0:
			x = (-b + disc['value'] ** (1/2.0)) / 2*a
			result['message'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = "
			result['value'] = x
		else:
			x1 = (-b + disc['value'] ** (1/2.0)) / 2*a
			x2 = (-b - disc['value'] ** (1/2.0)) / 2*a
			result['message'] = "Квадратное уравнение имеет два действительных корня: " 
			result['value'] = "x1 = %.1f, x2 = %.1f" % (x1, x2)


	context = {"param_a":param_a, "param_b":param_b, "param_c":param_c, "disc":disc, \
			"result":result, 'a':{'message':'a = '}, 'b':{'message':'b = '}, \
			'c':{'message':'c = '}}
	
	if 'a' in locals():
		context['a']['value'] = a
	if 'b' in locals():
		context['b']['value'] = b
	if 'c' in locals():
		context['c']['value'] = c
	return render(request,'results.html', context)