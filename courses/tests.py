# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client

from courses.models import Course

class CoursesListTest(TestCase):

    def test_list(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_content(self):
        course1 = Course.objects.create(
            name = 'Django Base',
            short_description = 'Django Base Course')
        course2 = Course.objects.create(
            name = 'Python Base',
            short_description = 'Python Base Course')
        client = Client()
        response = client.get('/')
        self.assertEqual(Course.objects.all().count(), 2)

    def test_404(self):
        client = Client()
        course1 = Course.objects.create(
            name = 'Django Base',
            short_description = 'Django Base Course')
        response = client.get('/courses/2/')
        self.assertEqual(response.status_code, 404)

    def test_titles(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Курсы PyBursa')
        self.assertContains(response, 'Program')

    def test_template(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')