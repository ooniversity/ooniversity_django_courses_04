# -*- coding: utf-8 -*-
from courses.models import Course
from courses.models import Lesson
from django.core.urlresolvers import reverse
from django.test import TestCase


class CoursesListTest(TestCase):

    def setUp(self):
        for course in ['Django', 'RoR', 'Spring']:
            Course.objects.create(name=course)

    def get_response(self):
        return self.client.get(reverse('index'))

    def test_course_list_response(self):
        self.assertEqual(self.get_response().status_code, 200)

    def test_index_template(self):
        self.assertTemplateUsed('index.html')

    def test_list_count(self):
        self.assertEqual(self.get_response().context['courses'].count(), 3)

    def test_course_list_template_contains(self):
        self.assertContains(self.get_response(), 'Bursa')

    def test_active_link(self):
        self.assertContains(self.get_response(), """<li class="active"><a href="/">Main</a></li>""")


class CoursesDetailTest(TestCase):

    def setUp(self):
        course = Course.objects.create(name='DJANGO')
        for lesson in self.get_lessons():
            Lesson.objects.create(course=course, subject=lesson)

    def get_response(self):
        course = Course.objects.get(id=1)
        return self.client.get('/courses/{}/'.format(course.id))

    def test_detail_response(self):
        self.assertEqual(self.get_response().status_code, 200)

    def test_course_detail_template(self):
        self.assertTemplateUsed(self.get_response(), 'courses/detail.html')

    def test_course_unicode(self):
        self.assertEqual(Course.objects.get(name='DJANGO').__unicode__(), self.get_response().context['course'].name)

    def test_lessons_context(self):
        for lesson in self.get_lessons():
            self.assertContains(self.get_response(), '{}'.format(lesson))

    def test_exist_course_students_link(self):
        self.assertContains(self.get_response(), """<a href="/students/?course_id={}">Students</a>""".format(1))

    def get_lessons(self):
        return ('Django first steps', 'Структура Web приложения', 'Работа с базами данных ORM')
