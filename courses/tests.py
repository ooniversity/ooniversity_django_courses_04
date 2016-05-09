from django.test import TestCase
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User
from django.test import Client

def add_course():
    coach1=Coach.objects.create(
            user=User.objects.create(),
            date_of_birth='1986-11-11',
            gender='F',
            phone='0985641245',
            address='Kharkov',
            skype='stud1')
             
    course1 = Course.objects.create(
            name='course1',
            short_description='description',
            description='full description',
            coach=coach1,
            assistant=coach1) 
class CoursesListTest(TestCase):
    def test_course_valid_links(self):
		response = self.client.get('/')
		self.assertContains(response, 'Main')
		self.assertContains(response, 'Contacts')
		self.assertContains(response, 'Students')
    
        
    def test_course_list_code(self):
        client = Client()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_course_list_number(self):
        client = Client()
        response = self.client.get('/')
        self.assertEqual(Course.objects.all().count(), 0) 
    def test_course_list_codenot(self):
        add_course()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_course_list_numbernot(self):
        add_course()
        response = self.client.get('/')
        self.assertEqual(Course.objects.all().count(), 1)
    def test_course_list_template(self):
        client = Client()
        add_course()
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
    def test_valid_course_name_edit(self):
        client = Client()
        add_course()
        response = self.client.get('/courses/edit/1/')
        self.assertContains(response, 'SomeCourse')  
              
class CoursesDetailTest(TestCase):
    def test_course_valid_link(self):
		response = self.client.get('/')
		self.assertContains(response, 'Main')
		self.assertContains(response, 'Contacts')
		self.assertContains(response, 'Students')
    def test_course_create(self):
        client = Client()
        add_course()
        self.assertEqual(Course.objects.all().count(), 1)  
    def test_course_detail_view0(self):
        client = Client()
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
    def test_course_detail_view(self):
        client = Client() 
        add_course()
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        
        
    def test_course_edit(self):
        client = Client()
        add_course()
        response = self.client.get('/courses/edit/1/')
        
        response = self.client.post('/courses/edit/1/', {'name': 'Course1_1', 'short_description': 'description_1', 'description': 'full_description_1'})
        self.assertEqual(response.status_code, 302)
    def test_course_detail_name(self):
        client = Client()
        add_course()
        response = self.client.get('/courses/1/')
            
        self.assertContains(response, 'SomeCourse') 
    def test_course_detail_description(self):
        client = Client()
        add_course()
        response = self.client.get('/courses/1/')
           
        self.assertContains(response, 'SomeBigDescription')
     
    def test_course_detail_template(self):
        client = Client()
        add_course()
        response = self.client.get('/courses/1/')
        self.assertTemplateUsed(response, 'courses/detail.html')

