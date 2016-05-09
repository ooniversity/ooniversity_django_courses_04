from django.test import TestCase
from django.test import Client

from students.models import Student


def create_student(studentname):
    Student.objects.create(
        name=studentname,
        surname="Petrov",
        date_of_birth="1990-05-05",
        email="PPetrov@mail.ru",
        phone="12345678",
        address="my long address",
        skype="PPetrov",
    )


class StudentsListTest(TestCase):

    def test_list_statuscode(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_list_header(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Students')

    def test_list_url_active(self):
        client = Client()
        response = client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_pagination(self):
        for i in ['First', 'Second', 'Third']:
            create_student(i)
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'next >>')


class StudentsDetailTest(TestCase):

    def test_detail_create(self):
        create_student("Vasya")
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, "Vasya")

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
        for i in ['Vasya', 'Petya', 'Lena']:
            create_student(i)
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'Vasya Petrov')

    def test_detail_url_active(self):
        for i in ['First', 'Second', 'Third']:
            create_student(i)
        client = Client()
        response = client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')
