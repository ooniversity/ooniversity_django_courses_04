# -*- coding: utf-8 -*-
from django.test import TestCase
from courses.models import Course
from django.test import Client


class CoursesListTest(TestCase):
    def test_list(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_list_curs(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Курсы PyBursa')
    def test_list_Description(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Description')
    def test_list_url(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')
    def test_create_course(self):
        client = Client()
        Course.objects.create(
            name='Python Base',
            short_description='Основы программирования Python')
        response = client.get('/')
        self.assertEqual(response.status_code, 200)


class CoursesDetailTest(TestCase):
    def test_detail_course1(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course1 = Course.objects.create(
            name = 'Python Base',
            short_description = 'Основы программирования Python')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course1.name)

    def test_detail_course2(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course2 = Course.objects.create(
            name = 'PythonExtended',
            short_description = 'Расширенный курс Python')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course2.name)

    def test_detail_course3(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course3 = Course.objects.create(
            name = 'Python Full',
            short_description = 'Полный курс Python')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course3.name)

    def test_detail_course4(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course4 = Course.objects.create(
            name = 'Python Gold',
            short_description = 'Золотая серия курсов. Для избранных.')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course4.name)

    def test_detail_course_lesson(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course1 = Course.objects.create(
            name = 'Python Base',
            short_description = 'Основы программирования Python')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Добавить новое занятие')