# -*- coding: utf-8 -*-
from courses.models import Course
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.test import TestCase

class CoursesListTest(TestCase):

    def setUp(self):
        Course.objects.create(name='DJANGO')

    def get_response(self):
        return self.client.get(reverse('index'))

    def test_course_list_response(self):
        self.assertEqual(self.get_response().status_code, 200)

    def test_index_template(self):
        with self.assertTemplateUsed('index.html'):
            render_to_string('index.html')

    def test_list_count(self):
        self.assertEqual(self.get_response().context['courses'].count(), 1)

    def test_course_list_template_contains(self):
        self.assertContains(self.get_response(), "Bursa",
                            status_code=200)


class CoursesDetailTest(TestCase):

    # def setUp(self):
    #     Course.objects.create(name='DJANGO')

    def get_response(self):
        return self.client.get(reverse('courses:detail'))

    def test_detail_response(self):
        self.assertEqual(self.get_response().status_code, 200)

    def test_detail_template(self):
        with self.assertTemplateUsed('courses/detail.html'):
            render_to_string('courses/detail.html')

    def test_course_unicode(self):
        self.assertEqual(Course.objects.get(name='DJANGO').__unicode__(), self.get_response().context['course'].name)

