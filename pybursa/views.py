#from django.shortcuts import render_to_response
from django.shortcuts import render
from courses.models import Course, Lesson


#def index(request):	
#	return render_to_response('index.html')

#def contact(request):	
#	return render_to_response('contact.html')

#def student_list(request):	
#	return render_to_response('student_list.html')

#def student_detail(request):	
#	return render_to_response('student_detail.html')

def index(request):
    dic_for_cour = dict()
    for item_cour in Course.objects.all():
        dic_for_cour[item_cour.id] = [item_cour.name, item_cour.short_description]
    print (dic_for_cour)
    return render(request, 'index.html', {'course':dic_for_cour})

def contact(request):	
	return render(request, 'contact.html')

def student_list(request):	
	return render(request, 'student_list.html')

def student_detail(request):	
	return render(request, 'student_detail.html')