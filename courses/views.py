from django.views.generic.detail import DetailView
from courses.models import Course


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"
