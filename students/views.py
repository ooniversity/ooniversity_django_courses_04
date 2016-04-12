from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from courses.models import Course
from students.models import Student


class StudentListView(ListView):
    model = Student
    template_name = "students/list.html"

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses__id=course_id)
        else:
            students = Student.objects.all()
        return students


class StudentDetailView(DetailView):
    model = Student
    template_name = "students/detail.html"

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(student__id=self.object.id)
        return context
