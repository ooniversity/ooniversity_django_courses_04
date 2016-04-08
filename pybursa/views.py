from django.shortcuts import  render



def index(request):
    print 'Start index view!'
    return render(request, 'index.html')

def contact(request):
    print 'Start contact view!'
    return render(request, 'contact.html')

def student_list(request):
    print 'Start student_list view!'
    return render(request, 'student_list.html')

def student_detail(request):
    print 'Start student_detail view!'
    return render(request, 'student_detail.html')