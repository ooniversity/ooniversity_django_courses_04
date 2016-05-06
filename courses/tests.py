
# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from courses.models import Course

class CoursesListTest(TestCase):
	def test_page(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_title(self):
		client = Client()
		response = client.get('/')
		self.assertContains(response, 'PyBursa')

	def test_corses(self):
		course1 = Course.objects.create(name='pyursa', short_description='Stady Pybursa')
		course2 = Course.objects.create(name='djabursa', short_description='Stady Djbursa')
		course3 = Course.objects.create(name='jsbursa', short_description='Stady Jsburs')
		self.assertEqual(Course.objects.all().count(), 3)

	def test_template(self):
		client = Client()
		response = client.get('/')
		self.assertTemplateUsed(response, 'index.html')

	def test_not_template(self):
		client = Client()
		response = client.get('/courses/1/')
		self.assertTemplateNotUsed(response, 404)
		