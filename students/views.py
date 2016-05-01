from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator

class StudentDetailView(DetailView):
    model = Student
    #student = Student.objects.get(id=student_id)
#    def get_context_data(self, student_id):
#        student = Student.objects.get(id=student_id)
#        return {'student': student}

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    success_message = "Student %(full_name)s has been successfully added."

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student Registration'
        return context

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    success_message = "Info on the student has been sucessfully changed."

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    success_message = "Student %(full_name)s has been successfully deleted."
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Delete Student'
        return context


#def detail(request, pk):
#    return detail_view(request, pk, Student)


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses__id=int(course_id))
        else:
            students = Student.objects.all()
        return students


#def list_view(request):
#    if request.GET:
#        students = Student.objects.filter(courses__id=int(request.GET['course_id']))
#    else:
#        students = Student.objects.all()
#    return render(request, 'students/list.html', {'students': students})


#def detail_view(request, student_id):
#    student = Student.objects.get(id=student_id)
#    return render(request, 'students/detail.html', {'student': student})

#def create(request):
#    if request.method == 'POST':
#        form = StudentModelForm(request.POST)
#        if form.is_valid:
#            item = form.save()
#            messages.success(request, "Student %s has been successfully added." % item.full_name())
#            return redirect('students:list_view')
#    else:
#        form = StudentModelForm()
#    return render(request, 'students/add.html', {'form': form})


#def edit(request, student_id):
#    item = Student.objects.get(id=student_id)
#    if request.method == 'POST':
#        form = StudentModelForm(request.POST, instance=item)
#        if form.is_valid():
#            item = form.save()
#            messages.success(request, "Info on the student has been sucessfully changed.")
#        return redirect('students:edit', student_id)
#    else:
#        form = StudentModelForm(instance=item)
#    return render(request, 'students/edit.html', {'form': form})

#def remove(request, student_id):
#    item = Student.objects.get(id=student_id)
#    print 'Enter remove'
#    if request.method == 'POST':
#        item.delete()
#        messages.success(request, "Info on %s has been sucessfully deleted." % item.full_name())
#        return redirect('students:list_view')
#    return render(request, 'students/remove.html', {'item': item})
