-*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from coaches.models import Coach
from django.test import Client
from courses.models import Course, Lesson


class StudentsListTest(TestCase): 
    def test_list_statuscode(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
 
    def test_list_content(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Список студентов')
 
    def test_list_activeurl(self):
        client = Client()
        response = client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')
    
    def test_list_template(self):
        response = self.client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_list_response(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
 
    def test_list_activeurl(self):
        response = self.client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')
		
	def test_list_addlink(self):
		response = self.client.get('/')
 		self.assertContains(response, '/students/add/')

class StudentsDetailTest(TestCase):

    def test_detail_create(self):
        create_student('new')
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'new')		
 
    def test_detail_student_statuscode(self):
        response = self.client.get('/students/%d'%get_random_student().id)
        self.assertEqual(response.status_code, 301)

    def test_detail_response(self):
        for page in ['1', '2', '3']:
            response = self.client.get('/students/%s/' % page)
            self.assertEqual(response.status_code, 200)
 
    def test_detail_incorrect_info(self):
        response = self.client.get('/students/12/')
        self.assertEqual(response.status_code, 404)
 
    def test_detail_activeurl(self):
        response = self.client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html') 
		
	def test_detail_response_statuscode(self):
        for page in ['1', '2']:
            response = self.client.get('/students/%s/' % page)
            self.assertEqual(response.status_code, 200)
 
    def test_detail_incorrect_student(self):
        response = self.client.get('/students/12/')
        self.assertEqual(response.status_code, 404)
