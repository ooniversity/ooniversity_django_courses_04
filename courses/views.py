from django.views.generic.detail import DetailView
from courses.models import Course, Lesson


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons_list'] = Lesson.objects.filter(course=self.object.id)
        return context
