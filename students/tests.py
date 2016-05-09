from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from courses.models import Course, Lesson
from students.models import Student
from coaches.models import Coach


def add_student():
    coach1=Coach.objects.create(
        user=User.objects.create(),
        date_of_birth='1986-11-11',
        gender='F',
        phone='0985641245',
        address='Kharkov',
        skype='stud1',
        description='description') 
    course1 = Course.objects.create(
        name='newcourse',
        short_description='description',
        description='full description',
        coach=coach1,
        assistant=coach1)
    course2 = Course.objects.create(
        name='course2',
        short_description='description2',
        description='full description2',
        coach=coach1,
        assistant=coach1)
    student1 = Student.objects.create(
        name = 'student1',
        surname = 'stud1',
        date_of_birth = '1988-01-07',
        email = 'student1@gmail.com',
        phone = '0975874562',
        address = 'Kyiv',
        skype = 'stud1')
    student1.courses.add(course1)
    student2 = Student.objects.create(
        name = 'student2',
        surname = 'stud2',
        date_of_birth = '1980-12-12',
        email = 'student2@gmail.com',
        phone = '0998745612',
        address = 'Odessa',
        skype = 'stud2')
    student2.courses.add(course2)

class StudentsListTest(TestCase):
    
    def test_student_valid_links(self):
		response = self.client.get('/students/')
		self.assertContains(response, 'Main')
		self.assertContains(response, 'Contacts')
		self.assertContains(response, 'Students')
    def test_student_list_code(self):
        client = Client()
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
    def test_student_list_number(self):
        client = Client()
        response = self.client.get('/students/')
        self.assertEqual(Student.objects.all().count(), 0) 
    def test_student_list_codenot(self):
        client = Client()
        add_student()
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
    def test_student_list_numbernot(self):
        client = Client()
        add_student()
        response = self.client.get('/students/')
        self.assertEqual(Student.objects.all().count(), 2)
    def test_student_list_template(self):
        client = Client()
        add_student()
        response = self.client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')
    def test_valid_student_name_edit(self):
        client = Client()
        add_student()
        response = self.client.get('/students/edit/1/')
        self.assertContains(response, 'student1')
    def test_student_title(self):
        client = Client()
        response = self.client.get('/students/')
        self.assertContains(response, 'Students')     
        
   
		
class StudentsDetailTest(TestCase):
    def test_student_valid_links2(self):
		response = self.client.get('/students/')
		self.assertContains(response, 'Main')
		self.assertContains(response, 'Contacts')
		self.assertContains(response, 'Students')
    def test_detail_name(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        
        self.assertContains(response, 'student1')  
    def test_detail_surname(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        
        self.assertContains(response, 'st1') 
    def test_detail_address(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        
        self.assertContains(response, 'City')
    def test_detail_skype(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        
        self.assertContains(response, 'stskype1') 
    def test_student_detail_template(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        self.assertTemplateUsed(response, 'students/student_detail.html')
    def test_detail_phone(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        self.assertContains(response, '0-800-900-500-67') 

