# -*- coding: utf-8 -*-
from django.test import TestCase
from students.models import Student
from django.test import Client
from courses.models import Course

class StudentsListTest(TestCase):

	def test_student_create(self):
		''' Проверка на создание студента '''
		student1 = Student.objects.create(
							name='Ivan',
							surname='Ivanov',
							date_of_birth='1991-12-03')					
		self.assertEqual(Student.objects.all().count(), 1)

	def test_student_content(self):
		''' Проверка на содержание инфо в объекте студент'''
		student1 = Student.objects.create(
							name='Ivan',
							surname='Ivanov',
							date_of_birth='1991-12-03')
		client = Client()		
		response = client.get('/students/')
		self.assertContains(response, "Ivanov")

	def test_template(self):
		''' Проверяет, что указанный шаблон использовался при рендеринге ответа '''
		client = Client()		
		response = client.get('/students/')		
		self.assertTemplateUsed(response, 'students/student_list.html')

	def test_title(self):
		''' Проверка содержимого заголовка'''
		client = Client()		
		response = client.get('/students/')		
		self.assertContains(response, "List of students")

	def test_course_page_200(self):		
		''' Наличие загрузки страницы '''
		client = Client()		
		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)

class StudentsDetailTests(TestCase):
	''' Проверка на удачную загрузку страницы '''
	def test_pages(self):		
		student1 = Student.objects.create(
							name='Ivan',
							surname='Ivanov',
							date_of_birth='1991-12-03')
		client = Client()		
		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 200)

	def test_detail_404(self):
		''' Проверка на ошибку 404'''
		student1 = Student.objects.create(
							name='Ivan',
							surname='Ivanov',
							date_of_birth='1991-12-03')
		client = Client()		
		response = client.get('/students/2/')
		self.assertEqual(response.status_code, 404)

	def test_template(self):
		''' Проверяет, что указанный шаблон использовался при рендеринге ответа '''
		student1 = Student.objects.create(
							name='Ivan',
							surname='Ivanov',
							date_of_birth='1991-12-03')
		client = Client()		
		response = client.get('/students/1/')		
		self.assertTemplateUsed(response, 'students/student_detail.html')

	def test_title(self):
		''' Проверка содержимого заголовка'''
		student1 = Student.objects.create(
							name='Ivan',
							surname='Ivanov',
							date_of_birth='1991-12-03')
		client = Client()		
		response = client.get('/students/1/')		
		self.assertContains(response, "Student detail")

	def test_contain(self):
		''' Проверка содержимого cтудента '''
		student1 = Student.objects.create(
							name='Ivan',
							surname='Ivanov',
							date_of_birth='1991-12-03',
							address='Kharkov')
		client = Client()		
		response = client.get('/students/1/')		
		self.assertContains(response, "Kharkov")

'''
	def test_add_student(self):
		course1 = Course.objects.create(
							name='PyBursa02',
							short_description="Web development with Vetal")
		course = Course.objects.get(id=1)
		print 'My object course =>'
		print course
		student1 = Student.objects.create(
							name='Ivan',
							surname='Ivanov',
							date_of_birth='1991-12-03',
							)
		client = Client()		
		response = client.get('/students/?course_id=5')
		self.assertEqual(response.status_code, 200)
'''
