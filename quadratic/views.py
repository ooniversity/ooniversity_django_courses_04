<<<<<<< HEAD
# -*- coding: utf-8 -*-
from django.shortcuts import render

def quadratic_results(request):

	a = ''
	b = '' 
	c = '' 
	a_err = ''
	b_err = ''
	c_err = ''
	disc = {}
	text_result = {}

	try:
		a = int(request.GET['a'])
	except ValueError:
		if request.GET['a'].isalpha():
			a_err = u"коэффициент не целое число"
			a = request.GET['a']
		else:
			a_err = u"коэффициент не определен"

	try:
		b = int(request.GET['b'])
	except ValueError:
		if request.GET['b'].isalpha():
			b_err = u"коэффициент не целое число"
			b = request.GET['b']
		else:
			b_err = u"коэффициент не определен"

	try:
		c = int(request.GET['c'])
	except ValueError:
		if request.GET['c'].isalpha():
			c_err = u"коэффициент не целое число"
			c = request.GET['c']
		else:
			c_err = u"коэффициент не определен"


		if a == 0:
			a_err = u"коэффициент при первом слагаемом уравнения не может быть равным нулю"

	if not a_err and not b_err and not c_err :
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


	outtext = {"a_err":a_err, "b_err":b_err, "c_err":c_err, "disc":disc, "text_result":text_result, 'a':{'text':'a = ','value': a}, 'b':{'text':'b = ', 'value':b}, 'c':{'text':'c = ', 'value':c}}

	
	return render(request,'results.html', outtext)
=======
from django.shortcuts import render


def quadratic_results(request):
    data = {}
    d = x1 = x2 = None
    is_valid_parameters = True

    for k, v in request.GET.items():
        try:
            data[str(k)] = int(v)
        except ValueError:
            data[str(k)] = str(v)
            is_valid_parameters = False

    if is_valid_parameters and not data['a'] == 0:
        d = data['b'] ** 2 - 4 * data['a'] * data['c']
        if d == 0:
            x1 = x2 = -data['b'] / 2.0 * data['a']
        elif d > 0:
            x1 = (-data['b'] + d ** (1 / 2.0)) / (2 * data['a'])
            x2 = (-data['b'] - d ** (1 / 2.0)) / (2 * data['a'])

    sorted_data = sorted(data.items(), key=lambda x: x[0])
    return render(request, 'results.html', {'data': sorted_data, 'd': d, 'x1': x1, 'x2': x2})

>>>>>>> f114d78577c0d563bac959a439787d0446e06ff9
