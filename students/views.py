from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
import logging
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm

logger = logging.getLogger(__name__)

class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def  get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            course = get_object_or_404(Course, id=course_id)
            list_of_students = course.student_set.all()
        else:
            list_of_students = Student.objects.all()
        return list_of_students

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        context['course_id'] = self.request.GET.get('course_id', None)
        return context



class StudentDetailView(DetailView):
    model = Student
    logger.debug('Students detail view has been debugged')
    logger.info('Logger of students detail view informs you!')
    logger.warning('Logger of students detail view warns you!')
    logger.error('Students detail view went wrong!')

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        student = form.save()
        message =  u"Student %s %s has been successfully added." % (student.name, student.surname)
        messages.success(self.request, message)
        return super(StudentCreateView, self).form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        form.save()
        message =  u"Info on the student has been sucessfully changed."
        messages.success(self.request, message)
        return super(StudentUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('students:edit', args=[self.get_object().id])

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def delete(self, request, pk):
        student = self.get_object()
        message =  u"Info on %s %s has been sucessfully deleted." % (student.name, student.surname)
        student.delete()
        messages.success(self.request, message)
        return redirect('students:list_view')

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