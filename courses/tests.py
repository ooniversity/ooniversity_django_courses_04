# encoding: utf-8
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

from courses.models import Course, Coach



class CoursesListTest(TestCase):

    def test_list(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_course(self):
        client = Client()
        course1 = Course.objects.create(
                name = 'Python Pro',
                short_description = 'Python Django Pro')
        response = client.get('/')
        self.assertContains(response, 'Python')
        self.assertContains(response, 'Python Django Pro')

    def test_content(self):
        course1 = Course.objects.create(
                name = 'Python Django',
                short_description = 'Python Django Essensial')

        course2 = Course.objects.create(
                name = 'Python Pro',
                short_description = 'Python Django Pro')

        client = Client()
        response = client.get('/')
        self.assertEqual(Course.objects.all().count(), 2)


    def test_titles_contains(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'University')
        self.assertContains(response, 'Описание')

    def test_template_used(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')



class CoursesDetailTest(TestCase):

    def test_index(self):
        course1 = Course.objects.create(
                name = 'Python',
                short_description = 'Python Django Pro')
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_titles_detail(self):
        course1 = Course.objects.create(
                name = 'Python',
                short_description = 'Python Django Pro')
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, 'Python')
        self.assertContains(response, 'Преподаватели')

    def test_template_used(self):
        course1 = Course.objects.create(
                name = 'Python',
                short_description = 'Python Django Pro')
        client = Client()
        response = client.get('/courses/1/')
        self.assertTemplateUsed(response, 'courses/detail.html')

    def test_error_404(self):
        course1 = Course.objects.create(
                name = 'Python',
                short_description = 'Python Django Pro')
        client = Client()
        response = client.get('/courses/2/')
        self.assertEqual(response.status_code, 404)

    def test_coaches(self):
        user1 = User.objects.create(
                username = 'Nick',
                password = 'qwerty',
                first_name = 'Nick_1',
                last_name = 'Nick_2')
        coach1 = Coach.objects.create(
                date_of_birth = '1994-01-12',
                gender = 'M',
                phone = '444333',
                address = 'Address',
                skype = 'low.f',
                description = 'My description',
                user = user1)
        course1 = Course.objects.create(
                name = 'Python',
                short_description = 'Python Django Pro')

        coach1.coach_courses.add(course1)
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, 'Nick_1 Nick_2')
