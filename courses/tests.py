from django.test import TestCase
from django.test import Client

class CoursesListTest(TestCase):
	def test_page(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code, 200)