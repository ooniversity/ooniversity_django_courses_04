# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client


from students.models import Student
from courses.models import Course


class StudentsListTest(TestCase):
   
    
    def test_get_status_code_stlist(self):        
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_titles_stlist(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'Студенты курса PyBursa')

    def test_template_stlist(self):
        response = self.client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_create_student(self):
        student = Student.objects.create(
            name = u'Test',
            surname = u'Test',
            date_of_birth = u'1999-01-01',
            email = u'test@gmail.com',
            phone = 7653899,
            address = u'New-York',
            skype = u'testtt'
            )
        
        student1 = Student.objects.create(
            name = u'Test1',
            surname = u'Test1',
            date_of_birth = u'1999-11-11',
            email = u'test1@gmail.com',
            phone = 765389999,
            address = u'Los Angeles',
            skype = u'testtt1'
            )
        
        response = self.client.get('/students/')
        self.assertEqual(Student.objects.all().count(), 2)

    def test_pagination_stdlist(self):

        student = Student.objects.create(
            name = u'Test',
            surname = u'Test',
            date_of_birth = u'1999-01-01',
            email = u'test@gmail.com',
            phone = 7653899,
            address = u'New-York',
            skype = u'testtt'
            )
        
        student1 = Student.objects.create(
            name = u'Test1',
            surname = u'Test1',
            date_of_birth = u'1999-11-11',
            email = u'test1@gmail.com',
            phone = 765389999,
            address = u'Los Angeles',
            skype = u'testtt1'
            )

        student2 = Student.objects.create(
            name = u'Test2',
            surname = u'Test2',
            date_of_birth = u'1980-02-01',
            email = u'test2@gmail.com',
            phone = 874321,
            address = u'Detroit',
            skype = u'testttt2'
            )
        response = self.client.get('/students/')
        self.assertContains(response, 'next')



class StudentsDetailTest(TestCase):

    def test_get_status_code_stdetail(self):
        student = Student.objects.create(
            name = u'Test',
            surname = u'Test',
            date_of_birth = u'1999-01-01',
            email = u'test@gmail.com',
            phone = 7653899,
            address = u'New-York',
            skype = u'testtt'
            )        
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
     
    def test_get_stdetail_status_code(self):       
        response = self.client.get('/students/1')
        self.assertEqual(response.status_code, 301)

    def test_template_stdetail(self):
        student = Student.objects.create(
            name = u'Test',
            surname = u'Test',
            date_of_birth = u'1999-01-01',
            email = u'test@gmail.com',
            phone = 7653899,
            address = u'New-York',
            skype = u'testtt'
            )
        response = self.client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')

    def test_404_stdetail(self):
        student = Student.objects.create(
            name = u'Test',
            surname = u'Test',
            date_of_birth = u'1999-01-01',
            email = u'test@gmail.com',
            phone = 7653899,
            address = u'New-York',
            skype = u'testtt'
            )
        response = self.client.get('/students/2/')
        self.assertEqual(response.status_code, 404)

    def test_titles_stdetail(self):
        student = Student.objects.create(
            name = u'Test',
            surname = u'Test',
            date_of_birth = u'1999-01-01',
            email = u'test@gmail.com',
            phone = 7653899,
            address = u'New-York',
            skype = u'testtt'
            )        
        response = self.client.get('/students/1/')
        self.assertContains(response, u'Test Test')

