# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client

from students.models import Student

class StudentsListTest(TestCase):

    def test_list(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_content(self):
        student1 = Student.objects.create(
            name = 'Alex',
            surname = 'First',
            date_of_birth = '2000-02-10',
            email = 'aa@aa.aa',
            phone = 1111,
            address = 'Adress',
            skype = 'sk_ype',
            courses = '1'
            )
        course2 = Course.objects.create(
            name = 'Bob',
            surname = 'Second',
            date_of_birth = '1999-02-10',
            email = 'bb@bb.bb',
            phone = 2222,
            address = 'Adress2',
            skype = 'sk_ype2',
            courses = '2'
            )
        client = Client()
        response = client.get('/students/')
        self.assertEqual(Student.objects.all().count(), 2)

    def test_404(self):
        client = Client()
        student1 = Student.objects.create(
            name = 'Django Base',
            short_description = 'Django Base Course')
        response = client.get('/courses/2/')
        self.assertEqual(response.status_code, 404)

    def test_titles(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Список студентов')

    def test_template(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')