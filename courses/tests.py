# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

from courses.models import Course, Coach



class CoursesListTest(TestCase):
    
    def test_courlist(self):        
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_title_courlist(self):
        response = self.client.get('/')
        self.assertContains(response, u'Курсы от ITBursa')
        self.assertContains(response, u'Наши курсы')

    def test_template_courlist(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')


    def test_create_courlist(self):
        course = Course.objects.create(
            name = u'New Course',
            short_description = u'For advanced students'
            )

        course1 = Course.objects.create(
            name = u'Old course',
            short_description = u'For old student'
            )
        response = self.client.get('/')
        self.assertEqual(Course.objects.all().count(), 2)

    def test_content_courlist(self):
        course = Course.objects.create(
            name = u'New_Course',
            short_description = u'For advanced students',
            description = u'Course'
            )
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'New_Course')
    


class CoursesDetailTest(TestCase):
    
    def test_courdetail(self):
        course = Course.objects.create(
            name = u'New Course', 
            short_description = u'For advanced students'
            )        
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_template_courdetail(self):
        course1 = Course.objects.create(
            name = u'New Course',
            short_description = u'For advanced students')
        response = self.client.get('/courses/1/')
        self.assertTemplateUsed(response, 'courses/detail.html')

    def test_redirect_courdetail(self):
        course = Course.objects.create(
            name = u'New_Course',
            short_description = u'For advanced students',
            description = u'Course'
            )
        response = self.client.get('/courses/1')
        self.assertEqual(response.status_code, 301)

    def test_404_courdetail(self):

        course = Course.objects.create(
            name = u'New_Course',
            short_description = u'For advanced students',
            description = u'Course'
            )
        client = Client()
        response = client.get('/courses/2/')
        self.assertEqual(response.status_code, 404)

    def test_create_coach(self):
        user = User.objects.create(
            username = u'New_User',
            password = u'Ty6#00',
            first_name = u'Petro',
            last_name = u'Zachet')
        coach_new = Coach.objects.create(
            date_of_birth = u'1978-05-20',
            gender = u'M',
            phone = u'928347923874',
            address = u'Bangladesh',
            skype = u'turbo',
            description = u'New coach',
            user = user)
        course_new = Course.objects.create(
            name = u'New_Course',
            short_description = u'For advanced students')
        coach_new.coach_courses.add(course_new)
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'Petro Zachet')




