from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm

class StudentListView(ListView):
    model = Student

    def  get_queryset(self):
        if self.request.GET:
            course_id = int(self.request.GET['course_id'])
            course = get_object_or_404(Course, id=course_id)
            list_of_students = course.student_set.all()
        else:
            list_of_students = Student.objects.all()
        return list_of_students

class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context
		
		
#def detail(request, student_id):
#    student = get_object_or_404(Student, id=int(student_id))
#    student_courses_list = student.courses.all()
#    return render(request, 'students/detail.html', {'student':student, 'students_courses':student_courses_list})
 
#def list_view(request):
#    if request.GET:
#        course_id = int(request.GET['course_id'])
#        course = get_object_or_404(Course, id=course_id)
#        list_of_students = course.student_set.all()
#    else:
#       list_of_students = Student.objects.all()
#
#    return render(request, 'students/list.html', {'students_list': list_of_students})

#def create(request):
#    if request.method == "POST":
#        form = StudentModelForm(request.POST)
#        if form.is_valid():
#            application = form.save()
#            message =  u"Student %s %s has been successfully added." % (application.name, application.surname)
#            messages.success(request, message)
#            return redirect('students:list_view')
#    else:
#        form = StudentModelForm()
#    return render(request, 'students/add.html', {'form':form})

#def remove(request, student_id):
#    student = get_object_or_404(Student, id=student_id)
#    if request.method == "POST":
#        message =  u"Info on %s %s has been sucessfully deleted." % (student.name, student.surname)
#        student.delete()
#        messages.success(request, message)
#        return redirect('students:list_view')
#    else:
#        return render(request, 'students/remove.html', {'student':student})

#def edit(request, student_id):
#    student = get_object_or_404(Student, id=student_id)
#    if request.method == "POST":
#        form = StudentModelForm(request.POST, instance=student)
#        if form.is_valid():
#            form.save()
#            messages.success(request, u"Info on the student has been sucessfully changed.")
#            return render(request, 'students/edit.html', {'form':form})
#    else:
#        form = StudentModelForm(instance=student)
#    return render(request, 'students/edit.html', {'form':form})