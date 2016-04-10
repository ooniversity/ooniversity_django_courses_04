from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext


# Create your views here.
def quadratic_results(request):
	template = loader.get_template('results.html')
	a = request.GET['a']
	b = request.GET['b']
	c = request.GET['c']
    
	try:
		int(a)
		int(b)
		int(c)
	except:
		context = RequestContext(request, {'a': a, 'b': b, 'c': c, 'd': '', 'x1': 1, 'x2': 2})
		return HttpResponse(template.render(context))
	
	if a > '0' and b and c:
		d = get_discr(a, b, c)
	else:
		d = ''

	if d >= '0' and a and b:
		x1 = get_results(a, b, d)
		x2 = get_results(a, b, d, 2)
	elif d == '0' and a and b:
		x1 = x2 = get_results(a, b, d)
	else:
		x1 = x2 = 1
	context = RequestContext(request, {'a': a, 'b': b, 'c': c, 'd': d, 'x1': x1, 'x2': x2})
	return HttpResponse(template.render(context))


def get_results(a, b, d, order=1):
    if order == 1:
    	x = (-int(b) + int(d)**(1/2.0)) / 2*int(a)
    else:
    	x = (-int(b) - int(d)**(1/2.0)) / 2*int(a)
    return str(x)


def get_discr(a, b, c):
	return str(int(b)**2 - 4*int(a)*int(c))


def index(request):
	return HttpResponse("You are on the index page")