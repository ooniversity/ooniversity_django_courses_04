from django.shortcuts import render


def quadratic_results(request):
    text = "Hello!"
    return render(request, 'results.html', text)
