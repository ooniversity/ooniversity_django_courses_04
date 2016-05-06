# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

from courses.models import Course, Coach


class CoursesListTest(TestCase):

    def test_list(self):

        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_content(self):
        course1 = Course.objects.create(
            name = u'Django Base',
            short_description = u'Django Base Course')

        course2 = Course.objects.create(
            name = u'Python Base',
            short_description = u'Python Base Course')

        client = Client()
        response = client.get('/')
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course(self):

        client = Client()
        course1 = Course.objects.create(
            name = u'Django Base',
            short_description = u'Django Base Course')
        response = client.get('/')
        self.assertContains(response, 'Django Base')
        self.assertContains(response, 'Django Base Course')

    def test_titles(self):

        client = Client()
        response = client.get('/')
        self.assertContains(response, u'Курсы PyBursa')
        self.assertContains(response, u'Program')

    def test_template(self):

        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')

class CoursesDetailTest(TestCase):

    def test_detail(self):

        course1 = Course.objects.create(
            name = u'Django Base',
            short_description = u'Django Base Course')
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_titles_detail(self):

        course1 = Course.objects.create(
            name = u'Django Base',
            short_description = u'Django Base Course')
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, u'Django Base')
        self.assertContains(response, u'Преподаватели')

    def test_template_detail(self):
        course1 = Course.objects.create(
            name = u'Django Base',
            short_description = u'Django Base Course')
        client = Client()
        response = client.get('/courses/1/')
        self.assertTemplateUsed(response, 'courses/detail.html')

    def test_404_detail(self):

        course1 = Course.objects.create(
            name = u'Django Base',
            short_description = u'Django Base Course')
        client = Client()
        response = client.get('/courses/2/')
        self.assertEqual(response.status_code, 404)

    def test_coach(self):
        user1 = User.objects.create(
            username = u'User',
            password = u'111',
            first_name = u'Bob',
            last_name = u'Petrov')
        coach1 = Coach.objects.create(
            date_of_birth = u'2000-02-10',
            gender = u'M',
            phone = u'123123',
            address = u'Addres',
            skype = u'sk_pe',
            description = u'Some Text',
            user = user1)
        course1 = Course.objects.create(
            name = u'Django Base',
            short_description = u'Django Base Course')
        coach1.coach_courses.add(course1)
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, 'Bob Petrov')