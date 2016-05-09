# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

from coaches.models import Coach
from courses.models import Course, Lesson


def create_coach():
    Coach.objects.create(
        user=User.objects.create_user(
            username='teacher1',
            password='12345678',
            email='teacher1@gmail.com',
        ),
        date_of_birth='1980-04-04',
        gender='F',
        phone='123465798',
        address='Kharkov, Pushkinskaya st.1',
        skype='Teache1',
        description='Python Middle Developer',
    )


def create_course():
    Course.objects.create(
        name='newcourse',
        short_description='Short description of new course',
        description='Long description of new course',
        coach=Coach.objects.get(id=1),
        assistant=Coach.objects.get(id=1),
    )


def create_lesson(lesson_id):
    Lesson.objects.create(
        subject='lesson_' + str(lesson_id),
        description='shor description of new lesson',
        course=Course.objects.get(id=1),
        order=lesson_id,
    )


def create_full_course():
    create_coach()
    create_course()
    for i in range(3):
        create_lesson(i)


class CoursesListTest(TestCase):

    def test_list_statuscode(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_list_header(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Courses list')

    def test_list_url_active(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_create_coach(self):
        client = Client()
        create_coach()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_course(self):
        client = Client()
        create_coach()
        create_course()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_lesson(self):
        client = Client()
        create_full_course()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_list_content(self):
        client = Client()
        create_full_course()
        response = client.get('/')
        self.assertContains(response, 'NEWCOURSE')


class CoursesDetailTest(TestCase):

    def test_create_coach(self):
        client = Client()
        create_coach()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_course(self):
        client = Client()
        create_coach()
        create_course()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_lesson(self):
        client = Client()
        create_full_course()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_detail_redirect(self):
        create_full_course()
        client = Client()
        response = client.get('/courses/1')
        self.assertEqual(response.status_code, 301)

    def test_detail_statuscode(self):
        create_full_course()
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_detail_content_course(self):
        create_full_course()
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, 'newcourse')

    def test_detail_content_lessons(self):
        create_full_course()
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, 'lesson_2')
