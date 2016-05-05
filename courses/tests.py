from django.test import TestCase
from courses.models import Course, Lesson

# Create your tests here.
class CoursesListTest(TestCase):
	def test_cource_create(self):
		course1 = Course.objects.create(
							name = 'PyBursa2',
							short_description="Web development with django")
		self.assertEqual(Course.objects.all().count(),1)

	def 
	

#class CoursesDetailTest(TestCase):
#	def