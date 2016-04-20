# -*- coding: utf-8 -*-
import math
from django.shortcuts import render
from forms import QuadraticForm

def quadratic_results(request):

    if request.GET == {}:
        form = QuadraticForm()
        return render(request, 'quadratic/results.html', {"form" : form})


    

    if request.method == "GET":
        form = QuadraticForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data

            #a = request.GET['a']
            #b = request.GET['b']
            #c = request.GET['c']

            a = data['a']
            b = data['b']
            c = data['c']

           
            
            # 'warning_'+'a'
            dic = {'a': a, 'b': b, 'c': c}
            war_a = '' 
            war_b = ''
            war_c = ''       
            x = ''
            same_root = '' 
            des = ''
            des_warn = ''
            x1 = ''
            x2 = ''
            root_mes = ''
            x = ''
            same_root = '' 
            
            if a == '':
                a = ''
                war_a = 'коэффициент не определен'     
            

            elif a == '0':
                war_a = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'    
                        
            #elif not a.replace('-', '').isdigit():
            #elif not a.isdigit():
            #    war_a = 'коэффициент не целое число'
            
            if b == '':
                b = ''
                war_b = 'коэффициент не определен'
            
            #elif not b.replace('-', '').isdigit():
            #    war_b = 'коэффициент не целое число'

            if c == '':
                c = ''
                war_c = 'коэффициент не определен'

            #elif not c.replace('-', '').isdigit(): #last check if c=digit add check war_a and war_b
            #    war_c = 'коэффициент не целое число'

            if war_a == '' and war_b == '' and war_c == '':
                a = int(a)
                b = int(b)
                c = int(c)
                des = b**2-4*a*c

                if des < 0:
                    des_warn = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
                    x1 = ''
                    x2 = ''
                    root_mes = ''
                    x = ''
                    same_root = ''

                elif des == 0:
                    des_warn = ''
                    
                    x1 = ''
                    x2 = ''
                    root_mes = ''
                    x = (-b+math.sqrt(b**2-4*a*c))/2*a
                    same_root = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x
                else:
                    des_warn = ''
                    
                    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
                    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
                    root_mes = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2)

            

            s = {
                'a': a,
                'b': b, 
                'c': c, 
                'warning_a': war_a, 
                'warning_b': war_b, 
                'warning_c': war_c,
                'des': des,
                'des_warn': des_warn,
                'x1': x1,
                'x2': x2,
                'root_mes': root_mes,
                'x': x,
                'same_root': same_root,
                'form' : form
                }
            return render(request, 'quadratic/results.html', s)




        else:
            form = QuadraticForm(request.GET)
            return render(request, 'quadratic/results.html', {"form" : form})

    else:
        form = QuadraticForm()
        return render(request, 'quadratic/results.html', {"form" : form})



            




