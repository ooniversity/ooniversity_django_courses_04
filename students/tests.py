#-*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.contrib.auth.models import User
from courses.models import Course, Lesson
from coaches.models import Coach
from students.models import Student


class StudentsListTest(TestCase):

    def test_course_create(self):
        student1 = Student.objects.create(name = 'Olha', date_of_birth = '1987-08-06')
        self.assertEqual(Student.objects.all().count(), 1)

    def test_student_template_list(self):
        client = Client()
        student1 = Student.objects.create(name = 'Olha', date_of_birth = '1987-08-06', phone = '002020')
        response = client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')# проверка вызова шаблона
        self.assertContains(response, 'Olha')
        self.assertNotContains(response, '002020')

############################# проверить курс (временный тест)#####################################
    def test_student_course_list(self):
        client = Client()
        course1 = Course.objects.create(name = 'PyBursa', short_description = 'Web development')
        #student1 = Student.objects.create(name = 'Olha', date_of_birth = '1987-08-06', courses=course1)# ManyToMany
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PyBursa')
#########################################################################################

    def test_student_edit(self):
        client = Client()
        student1 = Student.objects.create(name = 'Olha', date_of_birth = '1987-08-06')
        student1 = Student.objects.update(name = 'Foma')
        response = client.get('/students/')
        self.assertEqual(Student.objects.all().count(), 1)
        #self.assertTemplateUsed(response, 'index.html')# проверка вызова шаблона   edit/2/
        self.assertContains(response, 'Foma')   

    def test_student_template_remove(self):
        #client = Client()
        student1 = Student.objects.create(name = 'Olha', date_of_birth = '1987-08-06')
        self.assertEqual(Student.objects.all().count(), 1)
        student1.delete()
        self.assertEqual(Student.objects.all().count(), 0)
        #response = client.get('/students/')
        #self.assertTemplateUsed(response, 'index.html')# проверка вызова шаблона 

class StudentDetailTest(TestCase):

    def test_student_detail(self):
        client = Client()
        student1 = Student.objects.create(name = 'Olha', date_of_birth = '1987-08-06', phone = '002020')
        response = client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')# проверка вызова шаблона
        self.assertContains(response, '002020')





