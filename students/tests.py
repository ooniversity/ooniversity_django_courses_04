# -*- coding: utf-8 -*-
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
            name = u'Django Base',
            short_description = u'Django Base Course')
        course2 = Course.objects.create(
            name = u'Python Base',
            short_description = u'Python Base Course')

        student1 = Student.objects.create(
            name = u'Alex',
            surname = u'First',
            date_of_birth = u'2000-02-10',
            email = u'aa@aa.aa',
            phone = 1111,
            address = u'Adress',
            skype = u'sk_ype'
            )
        course1.student_set.add(student1)
        course2.student_set.add(student1)

        student2 = Student.objects.create(
            name = u'Bob',
            surname = u'Second',
            date_of_birth = u'1999-02-10',
            email = u'bb@bb.bb',
            phone = 2222,
            address = u'Adress2',
            skype = u'sk_ype2'
            )
        course1.student_set.add(student2)

        client = Client()
        response = client.get('/students/')
        self.assertEqual(Student.objects.all().count(), 2)

    def test_404(self):

        client = Client()
        course1 = Course.objects.create(
            name = u'Django Base',
            short_description = u'Django Base Course')

        student1 = Student.objects.create(
            name = u'Alex',
            surname = u'First',
            date_of_birth = u'2000-02-10',
            email = u'aa@aa.aa',
            phone = 1111,
            address = u'Adress',
            skype = u'sk_ype'
            )
        course1.student_set.add(student1)
        response = client.get('/students/2/')
        self.assertEqual(response.status_code, 404)

    def test_titles(self):

        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Список студентов')

    def test_template(self):

        client = Client()
        response = client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

class StudentsDetailTest(TestCase):

    def test_detail_stud(self):

        student1 = Student.objects.create(
            name = u'Alex',
            surname = u'First',
            date_of_birth = u'2000-02-10',
            email = u'aa@aa.aa',
            phone = 1111,
            address = u'Adress',
            skype = u'sk_ype'
            )
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_titles_detail_stud(self):

        student1 = Student.objects.create(
            name = u'Alex',
            surname = u'First',
            date_of_birth = u'2000-02-10',
            email = u'aa@aa.aa',
            phone = 1111,
            address = u'Adress',
            skype = u'sk_ype'
            )
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, u'Alex First')

    def test_template_detail_stud(self):

        student1 = Student.objects.create(
            name = u'Alex',
            surname = u'First',
            date_of_birth = u'2000-02-10',
            email = u'aa@aa.aa',
            phone = 1111,
            address = u'Adress',
            skype = u'sk_ype'
            )
        client = Client()
        response = client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')

    def test_404_detail_stud(self):

        student1 = Student.objects.create(
            name = u'Alex',
            surname = u'First',
            date_of_birth = u'2000-02-10',
            email = u'aa@aa.aa',
            phone = 1111,
            address = u'Adress',
            skype = u'sk_ype'
            )
        client = Client()
        response = client.get('/students/2/')
        self.assertEqual(response.status_code, 404)

    def test_courses_stud(self):
        course1 = Course.objects.create(
            name = u'Django Base',
            short_description = u'Django Base Course')
        course2 = Course.objects.create(
            name = u'Python Base',
            short_description = u'Python Base Course')
        student1 = Student.objects.create(
            name = u'Alex',
            surname = u'First',
            date_of_birth = u'2000-02-10',
            email = u'aa@aa.aa',
            phone = 1111,
            address = u'Adress',
            skype = u'sk_ype'
            )
        course1.student_set.add(student1)
        course2.student_set.add(student1)
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'Django Base')
        self.assertContains(response, 'Python Base')