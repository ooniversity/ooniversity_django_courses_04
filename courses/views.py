from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect

from django.contrib import messages


from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

def detail(request, course_id):
	course = get_object_or_404(Course, id=int(course_id))
	lessons = Lesson.objects.filter(course_id=course_id)
	
	return render(request, 'courses/detail.html', locals())

def create(request):
    if request.method == "POST":
    	form = CourseModelForm(request.POST)
    	if form.is_valid():
    		course = form.save()
    		message = u"Course %s has been successfully added." % (course.name)
    		messages.success(request, message)
    		return redirect('/')
    else:
        form = CourseModelForm()	
    return render(request, 'courses/add.html', {'form':form}) 	

def remove(request, course_id):
	course = get_object_or_404(Course, id=course_id)
	if request.method == "POST":
	    message =  u"Course %s has been deleted." % (course.name)
	    course.delete()
	    messages.success(request, message)
	    return redirect('/')
	else:
	    return render(request, 'courses/remove.html', {'course':course})    

def edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "The changes have been saved.")
            return redirect('/')
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form':form})

def add_lesson(request):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            message = u"Lesson %s has been successfully added." % (lesson.subject)
            messages.success(request, message)
            return redirect('courses:detail', lesson.course.id )
    else:
        form = LessonModelForm()    
    return render(request, 'courses/add_lesson.html', {'form':form})       
