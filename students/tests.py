# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from students.models import Student

class StudentsListTest(TestCase):
	def test_page(self):
		client = Client()
		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)

	def test_template(self):
		client = Client()
		response = client.get('/students/')
		self.assertTemplateUsed(response, 'students/student_list.html')

	def test_title(self):
		client = Client()
		response = client.get('/students/')
		self.assertContains(response, 'Students list')

	def test_not_template(self):
		client = Client()
		response = client.get('/students/?page=2/')
		self.assertTemplateNotUsed(response, 404)

	def test_students(self):
		steudent1 = Student.objects.create(name='Юрий', surname='Махно', date_of_birth='2016-10-15')
		self.assertEqual(Student.objects.all().count(), 1)

class StudentsDetailTest(TestCase):
	def test_page(self):
		client = Client()
		steudent1 = Student.objects.create(name='Юрий', surname='Махно', date_of_birth='2016-10-15')
		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 200)

	def test_template(self):
		client = Client()
		steudent1 = Student.objects.create(name='Юрий', surname='Махно', date_of_birth='2016-10-15')
		response = client.get('/students/1/')
		self.assertTemplateUsed(response, 'students/student_detail.html')

	def test_title(self):
		client = Client()
		steudent1 = Student.objects.create(name='Юрий', surname='Махно', date_of_birth='2016-10-15')
		response = client.get('/students/1/')
		self.assertContains(response, 'Student Detail')

	def test_not_template(self):
		client = Client()
		steudent1 = Student.objects.create(name='Юрий', surname='Махно', date_of_birth='2016-10-15')
		response = client.get('/students/1/')
		self.assertTemplateNotUsed(response, 404)

	def test_redirect(self):
		client = Client()
		steudent1 = Student.objects.create(name='Юрий', surname='Махно', date_of_birth='2016-10-15')
		response = client.get('/students/1')
		self.assertEqual(response.status_code, 301)



