# -*- coding: utf-8 -*-
from django.shortcuts import render


def quadratic_results(request):
	text_a = text_b = text_c = str()
	disc = {}
	text_result = {}

	try:
		a = int(request.GET['a'])
	except ValueError:
		if request.GET['a'].isalpha():
			text_a = u"коэффициент не целое число"
			a = request.GET['a']
		else:
			text_a = u"коэффициент не определен"

	try:
		b = int(request.GET['b'])
	except ValueError:
		if request.GET['b'].isalpha():
			text_b = u"коэффициент не целое число"
			b = request.GET['b']
		else:
			text_b = u"коэффициент не определен"

	try:
		c = int(request.GET['c'])
	except ValueError:
		if request.GET['c'].isalpha():
			text_c = u"коэффициент не целое число"
			c = request.GET['c']
		else:
			text_c = u"коэффициент не определен"

	if 'a' in locals():
		if a == 0:
			text_a = u"коэффициент при первом слагаемом уравнения не может быть равным нулю"

	if not text_a and not text_b and not text_c :
		disc['message'] = "Дискриминант: "
		disc['value'] = b**2 - 4*a*c

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


	context = {"text_a":text_a, "text_b":text_b, "text_c":text_c, "disc":disc, \
			"text_result":text_result, 'a':{'message':'a = '}, 'b':{'message':'b = '}, \
			'c':{'message':'c = '}}
	
	if 'a' in locals():
		context['a']['value'] = a
	if 'b' in locals():
		context['b']['value'] = b
	if 'c' in locals():
		context['c']['value'] = c
	return render(request,'results.html', context)

