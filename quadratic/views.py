# encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
import math

def quadratic_results(request):
	#print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
    answer=''
    koef=[0]*3
    koef_names=('a','b','c')
    dont_solve_flag=False
    for i in range(0,3):
        koef[i]=request.GET.__getitem__(koef_names[i]) 
        if  koef[i]=='': 
            dont_solve_flag=True
            answer+= u'коэффициент не определен\n'
        elif  not koef[i].replace('-','0').isdigit(): 
            answer+= u'коэффициент не целое число\n'
            dont_solve_flag=True
        else:
            koef[i]=int(koef[i])
        if koef[i]==0 and i==0:
            dont_solve_flag=True
            answer+= u'коэффициент при первом слагаемом уравнения не может быть равным нулю\n'
    if dont_solve_flag:
        return render(request,'quadratic/results.html',{'responce':answer})    


    a,b,c = koef
    discr1= b*b - 4 * a * c
    answer+=u"Дескриминант: %d\n" % int(discr1)
    if discr1 > 0:
        x1 = (-b + math.sqrt(discr1)) / (2 * a)
        x2 = (-b - math.sqrt(discr1)) / (2 * a)
        answer+= u"Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f \n" % (x1,x2)
    elif discr1 == 0:
        x = -b / (2 * a)
        answer += u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f \n' % x
    else:
	    #print("Корней нет")
        answer += u"Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.\n"
    return render(request,'quadratic/results.html',{'responce':answer}) 

 

#return render(request,'result')

# Create your views here.
