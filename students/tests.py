from django.test import TestCase
from django.test import Client

from students.models import Student
from courses.models import Course

class StudentsListTest(TestCase):

	def test_students(self):
		client = Client()

		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)

		course = Course.objects.create(
			name = 'Course 1',
			short_description = 'Second test for course list',
			description = 'This is course number two')

		student = Student.objects.create(
			name = 'Example',
			surname = 'Examples',
			date_of_birth = '1990-05-04',
			email = 'asddsasd@gmail.com',
			phone = '0985635665',
			address = 'Vinnica',
			skype = 'vinna'
			)
		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)

	def test_students_count(self):
		client = Client()

		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)

		course = Course.objects.create(
			name = 'Course 1',
			short_description = 'Second test for course list',
			description = 'This is course number two')

		student = Student.objects.create(
			name = 'Example',
			surname = 'Examples',
			date_of_birth = '1990-05-04',
			email = 'asddsasd@gmail.com',
			phone = '0985635665',
			address = 'Vinnica',
			skype = 'vinna'
			)
		response = client.get('/students/')
		self.assertEqual(Course.objects.all().count(), 1)

	def test_students_name(self):
		client = Client()

		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)

		course = Course.objects.create(
			name = 'Course 1',
			short_description = 'Second test for course list',
			description = 'This is course number two')

		student = Student.objects.create(
			name = 'Example',
			surname = 'Examples',
			date_of_birth = '1990-05-04',
			email = 'asddsasd@gmail.com',
			phone = '0985635665',
			address = 'Vinnica',
			skype = 'vinna'
			)
		response = client.get('/students/')
		self.assertContains(response, 'Example')

	def test_student_course(self):
		client = Client()

		course = Course.objects.create(
			name = 'Course 1',
			short_description = 'Second test for course list',
			description = 'This is course number one')

		student = Student.objects.create(
			name = 'Example',
			surname = 'Examples',
			date_of_birth = '1990-05-04',
			email = 'asddsasd@gmail.com',
			phone = '0985635665',
			address = 'Vinnica',
			skype = 'vinna'
			)
		response = client.get('/students/?course_id=1')  
		self.assertEqual(response.status_code, 200)

	def test_student_skype(self):
		client = Client()

		student = Student.objects.create(
			name = 'Example',
			surname = 'Examples',
			date_of_birth = '1990-05-04',
			email = 'asddsasd@gmail.com',
			phone = '0985635665',
			address = 'Vinnica',
			skype = 'vinna'
			)
		response = client.get('/students/')  
		self.assertContains(response, 'vinna')


class StudentsDetailTest(TestCase):

	def test_student_empty(self):
		from django.test import Client
		client = Client()

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 404)

	def test_student_name(self):
		from django.test import Client
		client = Client()

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Course 1',
			short_description = 'Second test for course list',
			description = 'This is course number two')

		student = Student.objects.create(
			name = 'Example',
			surname = 'Examples',
			date_of_birth = '1990-05-04',
			email = 'asddsasd@gmail.com',
			phone = '0985635665',
			address = 'Vinnica',
			skype = 'vinna'
			)

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Example')

	def test_student_email(self):
		from django.test import Client
		client = Client()

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Course 1',
			short_description = 'Second test for course list',
			description = 'This is course number two')

		student = Student.objects.create(
			name = 'Example',
			surname = 'Examples',
			date_of_birth = '1990-05-04',
			email = 'asddsasd@gmail.com',
			phone = '0985635665',
			address = 'Vinnica',
			skype = 'vinna'
			)

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'asddsasd@gmail.com')

	def test_student_address(self):
		from django.test import Client
		client = Client()

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Course 1',
			short_description = 'Second test for course list',
			description = 'This is course number two')

		student = Student.objects.create(
			name = 'Example',
			surname = 'Examples',
			date_of_birth = '1990-05-04',
			email = 'asddsasd@gmail.com',
			phone = '0985635665',
			address = 'Vinnica',
			skype = 'vinna'
			)

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Vinnica')

	def test_student_skype(self):
		from django.test import Client
		client = Client()

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 404)

		course = Course.objects.create(
			name = 'Course 1',
			short_description = 'Second test for course list',
			description = 'This is course number two')

		student = Student.objects.create(
			name = 'Example',
			surname = 'Examples',
			date_of_birth = '1990-05-04',
			email = 'asddsasd@gmail.com',
			phone = '0985635665',
			address = 'Vinnica',
			skype = 'vinna'
			)

		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'vinna')
