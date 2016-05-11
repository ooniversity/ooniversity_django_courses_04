# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from students.models import Student, Course

def create_student(studentname):
    Student.objects.create(
        name=studentname,
        surname="Smirnov",
        date_of_birth="1991-01-01",
        email="smirnov@gmail.com",
        phone="77777",
        address="Bakulina str",
        skype="smirnov",
    )

class StudentsListTest(TestCase):

    def test_list(self):

        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        
    def test_titles(self):

        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Students')
        
    def test_template(self):

        client = Client()
        response = client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')
        
    def test_url_active(self):
        client = Client()
        response = client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')
        
    def test_create_content(self):
        create_student('Test')
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Test')
        
class StudentsDetailTest(TestCase):

    def test_detail_create(self):
        create_student("Ira")
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, "Ira")

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
        for i in ['Ira', 'Olya', 'Lena']:
            create_student(i)
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'Ira')

    def test_url_active(self):
        for i in ['First', 'Second', 'Third']:
            create_student(i)
        client = Client()
        response = client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')

