 # -*- coding: utf-8 -*-
from django.shortcuts import render
from forms import QuadraticForm


def quadratic_results(request):
	'''reshenie kvadratnogo uravneniya'''
	x,x1,x2 = 0, 0, 0
	koren, diskrimin = '', ''

	form = QuadraticForm()	
	if request.method == 'GET':
		form = QuadraticForm(request.GET)
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']
	
			diskriminant = b**2 - 4*a*c
			if diskriminant < 0:
				diskrimin = 'Дискриминант: %d' % diskriminant
				koren = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
		
			elif diskriminant == 0:
				x = -b/2.0*a
				diskrimin = 'Дискриминант: %d' % diskriminant
				koren = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' %x
		
			elif diskriminant > 0:
				x1 = (-b + diskriminant ** (1/2.0))/(2*a)
				x2 = (-b - diskriminant ** (1/2.0))/(2*a)
				diskrimin = 'Дискриминант: %d' % diskriminant
				koren = 'Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f' % (x1, x2)
	else:
		form = QuadraticForm()
	
	dic = {'form':form, 'x':x, 'x1':x1, 'x2':x2, 'diskrimin':diskrimin, 'koren':koren}
	return render(request, 'results.html', dic)
