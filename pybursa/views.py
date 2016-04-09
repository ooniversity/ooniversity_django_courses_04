from django.shortcuts import render

def index(request):
    return render(request, '../templates/index.html', )

def contact(request):
    return render(request, '../templates/contact.html', )

def student_list(request):
    return render(request, '../templates/student_list.html', )

def student_detail(request):
    return render(request, '../templates/student_detail.html', )            