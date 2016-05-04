# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test import Client

from students.models import Student


def create_student(st_name):
    Student.objects.create(
        name=st_name,
        surname="Иванов",
        date_of_birth="2085-05-04",
        email="Иван@Иванов.com",
        phone="1234567890",
        address="г. Харьков, ул. Иванова, д.36, кв.1",
        skype="ivanov",
    )


class StudentsListTest(TestCase):

    def test_list_statuscode(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_list_header(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Список студентов')

    def test_list_url_active(self):
        client = Client()
        response = client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_create_content(self):
        create_student('First')
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'First')

    def test_pagination(self):
        for i in ['First', 'Second', 'Third']:
            create_student(i)
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'next >>')


class StudentsDetailTest(TestCase):

    def test_detail_create(self):
        create_student('First')
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'First')

    def test_detail_statuscode(self):
        for i in ['First', 'Second', 'Third']:
            create_student(i)
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_detail_redirect(self):
        for i in ['First', 'Second', 'Third']:
            create_student(i)
        client = Client()
        response = client.get('/students/2')
        self.assertEqual(response.status_code, 301)

    def test_detail_header(self):
        for i in ['First', 'Second', 'Third']:
            create_student(i)
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'Student First Иванов detail')

    def test_detail_url_active(self):
        for i in ['First', 'Second', 'Third']:
            create_student(i)
        client = Client()
        response = client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')

    def test_detail_content(self):
        for i in ['First', 'Second', 'Third']:
            create_student(i)
        client = Client()
        response = client.get('/students/3/')
        self.assertContains(response, 'Third Иванов')
