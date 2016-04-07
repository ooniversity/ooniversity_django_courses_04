# -*- coding: utf-8 -*-
from django.shortcuts import render

def quadratic_results(request):
	text_a = ""
	text_b = ""
	text_c = ""
	text_result = ""
	text_disc = ""

	try:
		a = int(request.GET['a'])
	except ValueError:
		if request.GET['a'].isalpha():
			text_a = "коэффициент не целое число"
			a = request.GET['a']
		else:
			text_a = "коэффициент не определен"
			a = ""

	try:
		b = int(request.GET['b'])
	except ValueError:
		if request.GET['b'].isalpha():
			text_b = "коэффициент не целое число"
			b = request.GET['b']
		else:
			text_b = "коэффициент не определен"
			b = ""

	try:
		c = int(request.GET['c'])
	except ValueError:
		if request.GET['c'].isalpha():
			text_c = "коэффициент не целое число"
			c = request.GET['c']
		else:
			text_c = "коэффициент не определен"
			#c = ""

	if a == 0:
		text_a = "коэффициент при первом слагаемом уравнения не может быть равным нулю"

	if not text_a and not text_b and not text_c :
		disc = b**2 - 4*a*c
		text_disc = "Дискриминант: %d" % disc

		if disc < 0:
			text_result = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
		elif disc == 0:
			x1 = (-b + disc ** (1/2.0)) / 2*a
			text_result = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f" % x1
		else:
			x1 = (-b + disc ** (1/2.0)) / 2*a
			x2 = (-b - disc ** (1/2.0)) / 2*a
			text_result = "Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f" % (x1, x2)

	context = {"text_a":text_a, "text_b":text_b, "text_c":text_c, "text_disc":text_disc, "text_result":text_result}
	if 'a' in locals():
		context['a'] = a
	if 'b' in locals():
		context['b'] = b 
	if 'c' in locals():
		context['c'] = c
	return render(request,'results.html', context)