 # -*- coding: utf-8 -*-
from django.shortcuts import render

def quadratic_results(request):
	x,x1,x2,diskrimin = 0, 0, 0, 0
	no_koef_a, no_koef_b, no_koef_c= '','',''
	koef_not_int_a, koef_not_int_b, koef_not_int_c= '','',''
	if_a_0 = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
	diskr_less_0, dva_kornya, odin_koren = '','',''
	
	dic = request.GET
	try:
	    a = int(dic.get('a'))
	except ValueError:
		if (dic.get('a')) == '':
			no_koef_a = 'коэффициент не определен'
		else:
			koef_not_int_a = 'коэффициент не целое число'
		a = (dic.get('a'))

	try:
	    b = int(dic.get('b'))
	except ValueError:
		if (dic.get('b')) == '':
			no_koef_b = 'коэффициент не определен'
		else:
			koef_not_int_b = 'коэффициент не целое число'
		b = (dic.get('b'))

	try:
	    c = int(dic.get('c'))
	except ValueError:
		if (dic.get('c')) == "''":
			no_koef_c = 'коэффициент не определен'
		else:
			koef_not_int_c = 'коэффициент не целое число'
		c = (dic.get('c'))
	
	if type(a)==int and type(b)==int and type(c)==int:
		diskriminant = b**2 - 4*a*c
		if diskriminant < 0:
			diskrimin = 'Дискриминант: %s' % diskriminant
			diskr_less_0 = 'Дискриминант мненьше нуля, квадратное уровнение не имеет действительных корней'
			
		elif diskriminant == 0:
			x = -b/2.0*a
			diskrimin = 'Дискриминант: %s' % diskriminant
			odin_koren = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень x1 = x2 = %.1f' %x
		
		elif diskriminant > 0:
			try:
				x1 = (-b + diskriminant ** (1/2.0))/(2*a)
				x2 = (-b - diskriminant ** (1/2.0))/(2*a)
				diskrimin = 'Дискриминант: %s' % diskriminant
				dva_kornya = 'Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f' % (x1, x2)

			except ZeroDivisionError:
				return render(request, 'results.html', {'a':a,'b':b, 'c':c, 'if_a_0':if_a_0})
    		
    
	dic = {'a':a, 'b':b, 'c':c, 'x':x, 'x1':x1, 'x2':x2, 'no_koef_a':no_koef_a, 'no_koef_b':no_koef_b, 'no_koef_c':no_koef_c, 'koef_not_int_a':koef_not_int_a, 'koef_not_int_b':koef_not_int_b, 'koef_not_int_c':koef_not_int_c,
	       'diskr_less_0':diskr_less_0, 'diskrimin':diskrimin, 'dva_kornya':dva_kornya, 'odin_koren':odin_koren}
	return render(request, 'results.html', dic)
	
    	
