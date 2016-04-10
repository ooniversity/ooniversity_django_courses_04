# -*- coding: utf-8 -*-
from django.shortcuts import render

def quadratic_results(request):
	a_param = str()
	b_param = str()
	c_param = str()
	results = {}
	disc = {}
	

	try:
		a = int(request.GET['a'])
	except ValueError:
		if request.GET['a'].isalpha():
			a_param = u"коэффициент не целое число"
			a = request.GET['a']
		else:
			a_param = u"коэффициент не определен"

	try:
		b = int(request.GET['b'])
	except ValueError:
		if request.GET['b'].isalpha():
			b_param = u"коэффициент не целое число"
			b = request.GET['b']
		else:
			b_param = u"коэффициент не определен"

	try:
		c = int(request.GET['c'])
	except ValueError:
		if request.GET['c'].isalpha():
			c_param = u"коэффициент не целое число"
			c = request.GET['c']
		else:
			c_param = u"коэффициент не определен"

	if 'a' in locals():
		if a == 0:
			a_param = u"коэффициент при первом слагаемом уравнения не может быть равным нулю"

	if not a_param and not b_param and not c_param :
		disc['message'] = "Дискриминант: "
		disc['value'] = b**2 - 4*a*c

		if disc['value'] < 0:
			results['message'] = u"Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
		elif disc['value'] == 0:
			x = (-b + disc['value'] ** (1/2.0)) / 2*a
			results['message'] = u"Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = "
			results['value'] = x
		else:
			x1 = (-b + disc['value'] ** (1/2.0)) / 2*a
			x2 = (-b - disc['value'] ** (1/2.0)) / 2*a
			results['message'] = u"Квадратное уравнение имеет два действительных корня: " 
			results['value'] = u"x1 = %.1f, x2 = %.1f" % (x1, x2)


	context = {"a_param":a_param, "b_param":b_param, "c_param":c_param, "disc":disc, \
			"results":results, 'a':{'message':'a = '}, 'b':{'message':'b = '}, \
			'c':{'message':'c = '}}
	
	if 'a' in locals():
		context['a']['value'] = a
	if 'b' in locals():
		context['b']['value'] = b
	if 'c' in locals():
		context['c']['value'] = c
	return render(request,'results.html', context)