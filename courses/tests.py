-*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from coaches.models import Coach
from django.test import Client
from courses.models import Course, Lesson

 
def create_course():
    Course.objects.create(
        name='newcourse',
        short_description='Short description',
        description='full course description',
        coach=Coach.objects.get(id=1),
        assistant=Coach.objects.get(id=1),
    )
		
def create_full_course():
    create_coach()
    create_course()
    for i in range(3):
        create_lesson(i)
			

def create_coach():
    Coach.objects.create(
    user=User.objects.create_user(
        username='NewCoach',
        password='55555',
        email='newcoach@gmail.com',
    ),
    date_of_birth='1978-12-09',
    gender='F',
    phone='0970330456',
    address='Kharkov, 12 Lenina st.',
    skype='Coach_1',
    description='Senior Python developer',
    )	

def create_lesson(lesson_id):
	Lesson.objects.create(
	    subject='lesson_' + str(lesson_id),
	    description='it is a new lesson',
	    course=Course.objects.get(id=1),
	    order=lesson_id,
    )
	 
class CoursesListTest(TestCase):

    def test_list_active_url(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')
			
		
	def test_list_page(self):
	    client = Client()
		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)

    def test_list_new_course(self):
        client = Client()
        create_coach()
        create_course()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
  
    def test_list_course_title(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, u'Сведенья о курсе - pyBursa')   

    def test_list_using_template(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')
		
    def test_list_set_of_tests(self):		
		client = Client()
 		response = client.get('/')
 		self.assertEqual(response.status_code, 200)
 		course1 = Course.objects.create(
			name = 'test 1',
			short_description = 'This is first courses test',
			description = '1 course')
		course2 = Course.objects.create(
			name = 'test 2',
			short_description = 'This is second courses test',
			description = '2 course')
        course3 = Course.objects.create(
			name = 'test 3',
			short_description = 'This is third courses test',
			description = '3 course')
		response = client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Course.objects.all().count(), 3)
 
	def test_list_addlink(self):
		response = self.client.get('/')
 		self.assertContains(response, '/courses/add/')

	def test_list_removelink(self):
		course = Course.objects.create(
 			name = 'test 3',
 			short_description = 'This is third courses test',
 			description = '3 course')
 		response = self.client.get('/')
 		self.assertContains(response, '/courses/remove/{}/'.format(course.id))
 
    def test_list_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

 

 
 
class CoursesDetailTest(TestCase):
 
    def test_detail_newcoach(self):
        client = Client()
        create_coach()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
 
    def test_detail_newcourse(self):
        client = Client()
        create_coach()
        create_course()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
 
    def test_detail_coursecontent(self):
        create_full_course()
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, 'course_1')   
 
    def test_detail_item(self):
 		client = Client()
 		response = client.get('/courses/1/')
 		self.assertEqual(response.status_code, 200)
 		course = Course.objects.create(
 			name = 'test 1',
 			short_description = 'This is first courses test',
 			description = '1 course')
 		response = client.get('/courses/1/')
 		self.assertEqual(response.status_code, 200)
 
 	def test_detail_coursedescription(self):
		client = Client()
 		response = client.get('/courses/2/')
 		self.assertEqual(response.status_code, 200)
 		course = Course.objects.create(
 			name = 'test 2',
 			short_description = 'This is second courses test',
 			description = '2 course') 
 		response = client.get('/courses/2/')
 		self.assertEqual(response.status_code, 200)
 		self.assertContains(response, course.description)
  
    def test_detail_response_statuscode(self):
        for page in ['1', '2', '3']:
            response = self.client.get('/courses/%s/' % page)
            self.assertEqual(response.status_code, 200)
 
    def test_detail_incorrect_course(self):
        response = self.client.get('/courses/10/')
        self.assertEqual(response.status_code, 404)
 