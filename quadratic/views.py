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
		text_a = "коэффициент не целое число"
	except IndexError:
		text_a = "коэффициент не определен"
	try:
		b = int(request.GET['b'])
	except ValueError:
		text_b = "коэффициент не целое число"
	except IndexError:
		text_b = "коэффициент не определен"
	try:
		c = int(request.GET['c'])
	except ValueError:
		text_c = "коэффициент не целое число"
	except IndexError:
		text_c = "коэффициент не определен"

	if a == 0 and text_a == "":
		text_a = "коэффициент при первом слагаемом уравнения не может быть равным нулю"

	if text_a and text_b and text_c :
		disc = b**2 - 4*a*c
		text_disc = "Дискриминант: %d" % disc

		if disc < 0:
			text_result = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
		elif disc == 0:
			x1 = (-b + disc ** (1/2.0)) / 2*a
			text_result = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.2f" % x1
		else:
			x1 = (-b + disc ** (1/2.0)) / 2*a
			x2 = (-b - disc ** (1/2.0)) / 2*a
			text_result = "Квадратное уравнение имеет два действительных корня: x1 = %.2f, x2 = %.2f" % (x1, x2)


	return render(request,'results.html', {"text_a":text_a, "text_b":text_b, "text_c":text_c, "text_disc":text_disc, "text_result":text_result, "a" : a, "b" : b, "c" : c})