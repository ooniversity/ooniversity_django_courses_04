from django.shortcuts import render
from quadratic.models import Parametr, Solution, TypeParametr
from quadratic.forms import QuadraticForm

def quadratic_results(request):
    form = QuadraticForm()
    if request.method == 'GET':
        form = QuadraticForm(request.GET)
        s = Solution.objects.all()
        if form.is_valid():
            form.cleaned_data
            p = Parametr.objects.all()
            p = Parametr(param_a = request.GET['a'], param_b = request.GET['b'], param_c = request.GET['c'])
            p.save() 

            a = int(p.param_a)
            b = int(p.param_b)
            c = int(p.param_c)

            d = b ** 2 - 4 * a * c
            #s = Solution(discr = d)

            if d > 0:
                x1 = (-b + d ** (1/2.0)) / (2*a)
                x2 = (-b - d ** (1/2.0)) / (2*a)
                s = Solution(discr = d, root1 = x1, root2 = x2)
            elif d < 0:
                x = ''
                s = Solution(discr = d)
            elif d==0:
                x = -b / 2.0*a
                s = Solution(discr = d, root1 = x)
            s.save()
            print s.discr, s.root1, s.root2,

    return render (request, 'results.html', {'form':form, 'solution':s})
