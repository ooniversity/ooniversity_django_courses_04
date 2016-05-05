# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from students.models import Student


class StudentsListTest(TestCase):
    def test_list_statuscode(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
    def test_list_url(self):
        client = Client()
        response = client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')
    def test_list_head1(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Студенты PyBursa 04')
    def test_list_head2(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Список студентов:')
    def test_students(self):
        client = Client()
        student = Student.objects.create(
            name = 'Иванович',
            surname = 'Миша',
            date_of_birth="2000-04-14",
            email="Mixa@mail.ru",
            phone="050",
            address="YNo",
            skype="MIHA",
            )
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Иванович')


class StudentsDetailTest(TestCase):
    def test_detail_create(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
    def test_detail_url(self):
        client = Client()
        student1 = Student.objects.create(
            name = 'Иванович',
            surname = 'Миша',
            date_of_birth="2000-04-14",
            email="Mixa@mail.ru",
            phone="050",
            address="YNo",
            skype="MIHA",
            )
        response = client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')
    def test_student1(self):
        client = Client()
        student1 = Student.objects.create(
            name = 'Иванович',
            surname = 'Миша',
            date_of_birth="2000-04-14",
            email="Mixa@mail.ru",
            phone="050",
            address="YNo",
            skype="MIHA",
            )
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Иванович')
    def test_student1_1(self):
        client = Client()
        student1 = Student.objects.create(
            name = 'Иванович',
            surname = 'Миша',
            date_of_birth="2000-04-14",
            email="Mixa@mail.ru",
            phone="050",
            address="YNo",
            skype="MIHA",
            )
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Миша')
    def test_student1_2(self):
        client = Client()
        student1 = Student.objects.create(
            name = 'Иванович',
            surname = 'Миша',
            date_of_birth="2000-04-14",
            email="Mixa@mail.ru",
            phone="050",
            address="YNo",
            skype="MIHA",
            )
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '050')
    def test_student1_3(self):
        client = Client()
        student1 = Student.objects.create(
            name = 'Иванович',
            surname = 'Миша',
            date_of_birth="2000-04-14",
            email="Mixa@mail.ru",
            phone="050",
            address="YNo",
            skype="MIHA",
            )
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'MIHA')