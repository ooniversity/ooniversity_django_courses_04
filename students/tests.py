from django.test import TestCase, Client

from students.models import Student


def new_student(name):
    Student.objects.create(
        name = name,
        surname = name + 'Surname',
        date_of_birth = '1980-01-01',
        email = name + '@example.com',
        phone='12345678',
        address = 'address',
        skype = name + '.skype',
    )

class StudentsListTest(TestCase):
    def test_statuscode(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_title(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'MyBursa | Student\'s List')

    def test_template(self):
        client = Client()
        response = client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_new_student_statuscode(self):
        client = Client()
        new_student('Petr')
        response = client.get('/students/')
        self.assertTrue(response.status_code == 200)

    def test_new_student_content(self):
        client = Client()
        new_student('Petr')
        response = client.get('/students/')
        self.assertContains(response, 'PetrSurname Petr')

    def test_new_student_content_page(self):
        client = Client()
        new_student('Petr')
        new_student('Ivan')
        new_student('Sergey')
        response = client.get('/students/', follow=True)
        self.assertContains(response, '<a href="?page=2">next</a>')

    def test_new_student_content_page2(self):
        client = Client()
        new_student('Petr')
        new_student('Ivan')
        new_student('Sergey')
        response = client.get('/students/?page=2', follow=True)
        self.assertContains(response, '<a href="?page=1">previous</a>')




class StudentsDetailTest(TestCase):

    def test_statuscode(self):
        client = Client()
        new_student('Petr')
        response = client.get('/students/1', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_title(self):
        client = Client()
        new_student('Petr')
        response = client.get('/students/1', follow=True)
        self.assertContains(response, 'MyBursa | Student Detail')

    def test_template(self):
        client = Client()
        new_student('Petr')
        response = client.get('/students/1', follow=True)
        self.assertTemplateUsed(response, 'students/student_detail.html')

    def test_new_student_statuscode(self):
        client = Client()
        new_student('Petr')
        response = client.get('/students/1', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_new_student_content1(self):
        client = Client()
        new_student('Petr')
        response = client.get('/students/1', follow=True)
        self.assertContains(response, 'Petr PetrSurname')

    def test_new_student_content2(self):
        client = Client()
        new_student('Petr')
        new_student('Ivan')
        new_student('Sergey')
        response = client.get('/students/2', follow=True)
        self.assertContains(response, 'Ivan IvanSurname')

    def test_new_student_content3(self):
        client = Client()
        new_student('Petr')
        new_student('Ivan')
        new_student('Sergey')
        response = client.get('/students/3', follow=True)
        self.assertContains(response, 'Sergey SergeySurname')
