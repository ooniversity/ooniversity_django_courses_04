from django.shortcuts import render

def quadratic_results(request):
    #print request.GET
    print request.GET['a']
    b=(request.GET['a'])
    print b.isdigit()
    c=int(b)
    print type(c) 
    
    return render (request, 'results.html')
