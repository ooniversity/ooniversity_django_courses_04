#from django.shortcuts import render_to_response
from django.shortcuts import render


#def index(request):	
#	return render_to_response('index.html')

#def contact(request):	
#	return render_to_response('contact.html')

#def student_list(request):	
#	return render_to_response('student_list.html')

#def student_detail(request):	
#	return render_to_response('student_detail.html')

def index(request):	
	return render(request, 'index.html')

def contact(request):	
	return render(request, 'contact.html')

def student_list(request):	
	return render(request, 'student_list.html')

def student_detail(request):	
	return render(request, 'student_detail.html')