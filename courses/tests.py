# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from courses.models import Course, Lesson, Coach
# Create your tests here.


class CoursesListTest(TestCase):

    def test_zero_page(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, '')
        self.assertEqual(response.status_code, 200)

    def test_aad(self):
        client = Client()
        response = client.get('/courses/add/')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        client = Client()
        response = client.get('/courses/remove/1/')
        self.assertEqual(response.status_code, 404)
        course1 = Course.objects.create(name='Pybursa', short_description='hello students of python')
        response = client.get('/courses/remove/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pybursa')
        course1.delete()
        response = client.get('/courses/remove/1/')
        self.assertEqual(response.status_code, 404)

    def test_edit(self):
        client = Client()
        response = client.get('/courses/edit/1/')
        self.assertEqual(response.status_code, 404)
        course1 = Course.objects.create(name='Pybursa', short_description='hello students of python')
        course1.short_description = 'NEW'
        course1.save()
        response = client.get('/courses/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'NEW')

    def test_main(self):
        client = Client()
        course1 = Course.objects.create(name='Pybursa', short_description='hello students of python')
        response = client.get('/courses/remove/1/')
        course1.save()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pybursa')


class CoursesDetailTest(TestCase):

    def test_page_working(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course1 = Course.objects.create(name='Pybursa', short_description='hello students of python')
        response = client.get('/courses/1/')
        course1.save()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pybursa')

    def test_add_lesson_page(self):
        client = Client()
        course1 = Course.objects.create(name='Pybursa', short_description='hello students of python')
        response = client.get('/courses/1/')
        course1.save()
        self.assertEqual(response.status_code, 200)
        response = client.get('/courses/1/add_lesson')
        self.assertEqual(response.status_code, 200)

    def test_add_lesson(self):
        client = Client()
        course1 = Course.objects.create(name='Pybursa', short_description='hello students of python')
        response = client.get('/courses/1/')
        course1.save()
        self.assertEqual(response.status_code, 200)
        lesson1 = Lesson.objects.create(subject='PyBursa', description='just for test', order='1', course_id=1)
        response = client.get('/courses/1/')
        lesson1.save()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just for test')

    def test_coach_course(self):
        from django.contrib.auth.models import User
        client = Client()
        course1 = Course.objects.create(name='Pybursa', short_description='hello students of python')
        response = client.get('/courses/1/')
        course1.save()
        self.assertEqual(response.status_code, 200)
        user = User.objects.create(first_name='John',
                                   last_name='Zaika',
                                   username='john',
                                   password='123',
                                   email='zaika.y.s@gmail.com')
        coach = Coach.objects.create(date_of_birth='1978-05-20', user=user)
        coach.coach_courses.add(course1)
        response = client.get('/courses/1/')
        self.assertContains(response, 'John')

    def test_assistant_course(self):
        from django.contrib.auth.models import User
        client = Client()
        course1 = Course.objects.create(name='Pybursa', short_description='hello students of python')
        response = client.get('/courses/1/')
        course1.save()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pybursa')
        user = User.objects.create(first_name='John',
                                   last_name='Zaika',
                                   username='john',
                                   password='123',
                                   email='zaika.y.s@gmail.com')
        assistant = Coach.objects.create(date_of_birth='1978-05-20', user=user)
        assistant.assistant_courses.add(course1)
        response = client.get('/courses/1/')
        self.assertContains(response, 'John')
