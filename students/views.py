from students.models import Student
from django.contrib import messages
from students.forms import StudentModelForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class StudentListView(ListView):
    model = Student
    
    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id:
            students_list = Student.objects.filter(courses__id = course_id)
        else:
            students_list = Student.objects.all()
        return students_list

class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    form_class = StudentModelForm
    model = Student

    def form_valid(self, form):
        valid = super(StudentCreateView, self).form_valid(form)
        if valid:
            student = self.request.POST
            message = "Student {} {} has been successfully added.".format(student['surname'], student['name'])
            messages.success(self.request, message)
        return valid

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

class StudentUpdateView(UpdateView):
    form_class = StudentModelForm
    model = Student

    def form_valid(self, form):
        valid = super(StudentUpdateView, self).form_valid(form)
        if valid:
            message = "Info on the student has been sucessfully changed."
            messages.success(self.request, message)
        return valid

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context
   
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        message = "Info on {} {} has been sucessfully deleted.".format(student.name, student.surname)
        messages.success(self.request, message)
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

