# -*- coding: utf-8 -*-
from django.test import TestCase
from coaches.models import Coach
from courses.models import Course, Lesson
from django.contrib.auth.models import User


class CoursesDetailTest(TestCase):
    fixtures = ['coaches']

    def test_create_coach(self):
        create_coach()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_course(self):
        create_coach()
        create_course()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_lesson(self):
        create_full_course()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_detail_redirect(self):
        create_full_course()
        response = self.client.get('/courses/1')
        self.assertEqual(response.status_code, 301)

    def test_detail_statuscode(self):
        create_full_course()
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_detail_content_course(self):
        create_full_course()
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'course_1')

    def test_detail_content_lessons(self):
        create_full_course()
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'lesson_2')


class CoursesListTest(TestCase):

    def test_list_statuscode(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_list_header(self):
        response = self.client.get('/')
        self.assertContains(response, 'Выбирай свой курс!')

    def test_list_url_active(self):

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_create_coach(self):
        create_coach()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_course(self):
        create_coach()
        create_course()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_lesson(self):
        create_full_course()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_list_content(self):
        create_full_course()
        response = self.client.get('/')
        self.assertContains(response, 'COURSE_1')


def create_coach():
    Coach.objects.create(
        user=User.objects.create_user(
            username='coach_1',
            password='coach_1',
            email='coach_1@coach.com',
        ),
        date_of_birth='2085-05-04',
        gender='M',
        phone='1234657980',
        address='Kharkov',
        skype='sash-pro',
        description='Developer',
    )


def create_course():
    Course.objects.create(
        name='course_1',
        short_description=' ',
        description=' ',
        coach=Coach.objects.get(id=1),
        assistant=Coach.objects.get(id=1),
    )


def create_lesson(lesson_id):
    Lesson.objects.create(
        subject='lesson_' + str(lesson_id),
        description=' ',
        course=Course.objects.get(id=1),
        order=lesson_id,
    )


def create_full_course():
    create_coach()
    create_course()
    for i in range(3):
        create_lesson(i)


