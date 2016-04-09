 # -*- coding: utf-8 -*-
from django.shortcuts import render

def quadratic_results(request):
	'''reshenie kvadratnogo uravneniya'''
	x,x1,x2 = 0, 0, 0
	no_koef_a, no_koef_b, no_koef_c= '','',''
	koef_not_int_a, koef_not_int_b, koef_not_int_c, if_a_0 = '','','',''
	diskr_less_0, dva_kornya, odin_koren, diskrimin = '','','',''
	
	try:
	   a = int(request.GET['a'])
	except ValueError:
		if (request.GET['a']).isalpha():
			koef_not_int_a = 'коэффициент не целое число'
		else:
			no_koef_a = 'коэффициент не определен'
		a = (request.GET['a'])

	try:
	    b = int(request.GET['b'])
	except ValueError:
		if (request.GET['b']).isalpha():
			koef_not_int_b = 'коэффициент не целое число'
		else:
			no_koef_b = 'коэффициент не определен'
		b = (request.GET['b'])

	try:
	    c = int(request.GET['c'])
	except ValueError:
		if (request.GET['c']).isalpha():
			koef_not_int_c = 'коэффициент не целое число'
		else:
			no_koef_c = 'коэффициент не определен'
		c = (request.GET['c'])

	

	if type(a)==int and type(b)==int and type(c)==int:
		diskriminant = b**2 - 4*a*c
		if a == 0:
			if_a_0 = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
		
		elif diskriminant < 0:
			diskrimin = 'Дискриминант: %d' % diskriminant
			diskr_less_0 = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
			
		elif diskriminant == 0:
			x = -b/2.0*a
			diskrimin = 'Дискриминант: %d' % diskriminant
			odin_koren = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' %x
		
		elif diskriminant > 0:
			x1 = (-b + diskriminant ** (1/2.0))/(2*a)
			x2 = (-b - diskriminant ** (1/2.0))/(2*a)
			diskrimin = 'Дискриминант: %d' % diskriminant
			dva_kornya = 'Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f' % (x1, x2)
			
	dic = {'a':a, 'b':b, 'c':c, 'x':x, 'x1':x1, 'x2':x2, 'no_koef_a':no_koef_a, 'no_koef_b':no_koef_b, 'no_koef_c':no_koef_c, 'koef_not_int_a':koef_not_int_a, 'koef_not_int_b':koef_not_int_b, 'koef_not_int_c':koef_not_int_c,
			'diskr_less_0':diskr_less_0, 'diskrimin':diskrimin, 'dva_kornya':dva_kornya, 'odin_koren':odin_koren, 'if_a_0':if_a_0}
	return render(request, 'results.html', dic)
