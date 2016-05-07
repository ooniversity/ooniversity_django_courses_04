# encoding: utf-8
from django.test import TestCase
from django.test import Client

from students.models import Student, Course



class StudentsListTest(TestCase):

    def test_list(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_content(self):
        course1 = Course.objects.create(
                name = 'Python',
                short_description = 'Python Django Pro')
        course2 = Course.objects.create(
                name = 'Python',
                short_description = 'Python Django Pro')

        student1 = Student.objects.create(
                name = 'Nick',
                surname = 'Surname',
                date_of_birth = '1992-11-12',
                email = 'aa@qwe.com',
                phone = 11111,
                address = 'Adress',
                skype = 'skype1'
                )
        course1.student_set.add(student1)
        course2.student_set.add(student1)

        student2 = Student.objects.create(
                name = 'Nick',
                surname = 'Surname',
                date_of_birth = '1939-01-04',
                email = 'aa@qwe.com',
                phone = 22222,
                address = 'Adress2',
                skype = 'skype2'
                )
        course1.student_set.add(student2)

        client = Client()
        response = client.get('/students/')
        self.assertEqual(Student.objects.all().count(), 2)

    def test_titles(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Список студентов')

    def test_pagination(self):
        student1 = Student.objects.create(
                name = 'Alex',
                surname = 'First',
                date_of_birth = '2000-02-10',
                email = 'aa@qwe.com',
                phone = 1111,
                address = 'Adress',
                skype = 'skype1'
                )

        student2 = Student.objects.create(
                name = 'Bob',
                surname = 'Second',
                date_of_birth = '1999-02-10',
                email = 'aa@qwe.com',
                phone = 2222,
                address = 'Adress2',
                skype = 'skype2'
                )

        student3 = Student.objects.create(
                name = 'Bob',
                surname = 'Second',
                date_of_birth = '1959-12-12',
                email = 'aa@qwe.com',
                phone = 2222,
                address = 'Adress',
                skype = 'skype3'
                )

        student4 = Student.objects.create(
                name = 'Bob',
                surname = 'Second',
                date_of_birth = '1959-12-12',
                email = 'aa@qwe.com',
                phone = 2222,
                address = 'Adress',
                skype = 'skype'
                )

        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'next')

    def test_template_used(self):
        client = Client()
        response = client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')





class StudentsDetailTest(TestCase):

    def test_titles_stud(self):
        student1 = Student.objects.create(
                name = 'Alex',
                surname = 'First',
                date_of_birth = '2000-02-10',
                email = 'aa@aa.aa',
                phone = 1111,
                address = 'Adress',
                skype = 'sk_ype'
                )
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, u'Alex First')

    def test_detail_stud(self):
        student1 = Student.objects.create(
                name = 'Alex',
                surname = 'First',
                date_of_birth = '2000-02-10',
                email = 'aa@aa.aa',
                phone = 1111,
                address = 'Adress',
                skype = 'sk_ype'
                )
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_template_stud(self):
        student1 = Student.objects.create(
                name = 'Alex',
                surname = 'First',
                date_of_birth = '2000-02-10',
                email = 'aa@aa.aa',
                phone = 1111,
                address = 'Adress',
                skype = 'sk_ype'
                )
        client = Client()
        response = client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')

    def test_courses_stud(self):
        course1 = Course.objects.create(
                name = 'Django Base',
                short_description = 'Django Base Course')
        course2 = Course.objects.create(
                name = 'Python Base',
                short_description = 'Python Base Course')
        student1 = Student.objects.create(
                name = 'Alex',
                surname = 'First',
                date_of_birth = '2000-02-10',
                email = 'aa@aa.aa',
                phone = 1111,
                address = 'Adress',
                skype = 'sk_ype'
                )
        course1.student_set.add(student1)
        course2.student_set.add(student1)
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'Django Base')
        self.assertContains(response, 'Python Base')

    def test_error404(self):
        student1 = Student.objects.create(
                name = 'Alex',
                surname = 'First',
                date_of_birth = '2000-02-10',
                email = 'aa@aa.aa',
                phone = 1111,
                address = 'Adress',
                skype = 'sk_ype'
                )
        client = Client()
        response = client.get('/students/2/')
        self.assertEqual(response.status_code, 404)
