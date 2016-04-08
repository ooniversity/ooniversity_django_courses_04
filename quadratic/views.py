from django.shortcuts import render


def quadratic_results(request):
	a = 'hgjgjh123'
	s = request.GET
	print s
	return render(request, 'results.html', {'a':a,})
