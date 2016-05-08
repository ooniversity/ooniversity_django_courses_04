# -*- coding: utf-8 -*-
from django.test import TestCase
from courses.models import Course, Lesson
from django.test import Client


class CoursesListTest(TestCase):
	def test_course_create(self):
		course1 = Course.objects.create(
							name='PyBursa02',
							short_description="Web development with Vetal")			
		self.assertEqual(Course.objects.all().count(), 1)

	def test_course_content(self):
		course1 = Course.objects.create(
							name='PyBursa02',
							short_description="Web development with Vetal")
		client = Client()		
		response = client.get('/')
		#print 'Содержание response =>'		
		#print type(response)
		self.assertContains(response, "Web Development")

	def test_template(self):
		client = Client()		
		response = client.get('/')
		self.assertTemplateUsed(response, 'index.html')

	def test_title(self):
		client = Client()		
		response = client.get('/')		
		self.assertContains(response, "Main")

	def test_course_page_404(self):		
		client = Client()		
		response = client.get('/courses/')
		self.assertEqual(response.status_code, 404)

	def test_course_page_200(self):		
		client = Client()		
		response = client.get('/')
		self.assertEqual(response.status_code, 200)


class CoursesDetailTest(TestCase):	
	''' Проверка на удачную загрузку страницы '''
	def test_pages(self):		
		client = Client()				

		course1 = Course.objects.create(
							name='PyBursa02',
							short_description="Web development with Vetal")
		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)

	def test_template(self):
		''' Проверяет, что указанный шаблон использовался при рендеринге ответа '''
		course1 = Course.objects.create(
							name='PyBursa02',
							short_description="Web development with Vetal")
		client = Client()		
		response = client.get('/courses/1/')		
		self.assertTemplateUsed(response, 'courses/detail.html')

	def test_title(self):
		''' Проверка содержимого заголовка'''
		course1 = Course.objects.create(
							name='PyBursa02',
							short_description="Web development with Vetal")
		client = Client()		
		response = client.get('/courses/1/')		
		self.assertContains(response, "Course detail")

	def test_add_lesson(self):
		''' Проверка создания урока для курса '''
		course1 = Course.objects.create(
							name='PyBursa02',
							short_description="Web development with Vetal")	
		course = Course.objects.get(id=1)
		#print 'My object course =>'
		#print course.id
		lesson1 = Lesson.objects.create(
							subject='Python',
							description="Web development",
							course=course,
							order=1)
		#print 'My object lesson =>'
		#print Lesson.objects.all().count()		
		self.assertEqual(Lesson.objects.all().count(), 1)

	def test_detail_404(self):
		''' Проверка на ошибку 404'''
		course1 = Course.objects.create(
							name='PyBursa02',
							short_description="Web development with Vetal")
		client = Client()
		response = client.get('/courses/2/')
		self.assertEqual(response.status_code, 404)
		
		
'''
class CourseTests(TestCase):
	def test_course_create(self):
		course1 = Course.objects.create(
							name='PyBursa02',
							short_description="Web development with Vetal")	
		
		self.assertEqual(Course.objects.all().count(), 1)

	def test_pages(self):
		from django.test import Client
		client = Client()
		
		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)

		course1 = Course.objects.create(
							name='PyBursa02',
							short_description="Web development with Vetal")
		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "PyBursa02")
'''
