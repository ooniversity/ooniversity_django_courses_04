from django.shortcuts import get_object_or_404, render
from courses.models import Course, Lesson

def detail(request, course_id):
    course_info = get_object_or_404(Course, id=int(course_id))
    lesson_list = Lesson.objects.filter(course_id=course_id)
    lesson_list.order_by('order')
    return render(request, 'courses/detail.html', {'lessons':lesson_list, 'course': course_info})