# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from courses.models import Course, Coach


class CoursesListTest(TestCase):

    def test_list(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_course(self):
        client = Client()
        course1 = Course.objects.create(
            name = u'Django Test Course',
            short_description = u'Django Test Course description')
        response = client.get('/')
        self.assertContains(response, 'Django Test Course')
        self.assertContains(response, 'Django Test Course description')
        
    def test_index_template(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        
    def test_url_active(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        
    def test_title(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, u'Курсы Python от PyBursa')
        
class CoursesDetailTest(TestCase):

    def test_list(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_course(self):
        client = Client()
        course1 = Course.objects.create(
            name = u'Django Test Course',
            short_description = u'Django Test Course description')
        response = client.get('/')
        self.assertContains(response, 'Django Test Course')
        self.assertContains(response, 'Django Test Course description')
        
    def test_index_template(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        
    def test_url_active(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        
    def test_title(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, u'Курсы Python от PyBursa')
        
        
