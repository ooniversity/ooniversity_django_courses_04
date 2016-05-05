#-*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.contrib.auth.models import User
from courses.models import Course, Lesson
from coaches.models import Coach


class CoursesListTest(TestCase):

    def test_course_create(self):
        course1 = Course.objects.create(name = 'PyBursa', short_description = 'Web development')
        self.assertEqual(Course.objects.all().count(), 1)

    def test_course_template_list(self):
        client = Client()
        course1 = Course.objects.create(name = 'PyBursa', short_description = 'Web development')
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')# проверка вызова шаблона
        self.assertContains(response, 'Web')

    def test_course_template_edit(self):
        client = Client()
        course1 = Course.objects.create(name = 'PyBursa', short_description = 'Web development')
        course1 = Course.objects.update(short_description = 'Description Python')
        response = client.get('/')
        self.assertEqual(Course.objects.all().count(), 1)
        self.assertTemplateUsed(response, 'index.html')# проверка вызова шаблона
        self.assertContains(response, 'Python') 

    def test_course_remove(self):
        course1 = Course.objects.create(name = 'PyBursa', short_description = 'Web development')
        self.assertEqual(Course.objects.all().count(), 1)
        course1.delete()
        self.assertEqual(Course.objects.all().count(), 0)


    def test_course_template_remove(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')# проверка вызова шаблона

        #self.assertRedirects(response, '/home', status_code=301, target_status_code=301)


 
 

class CoursesDetailTest(TestCase):

    def test_course_page(self):
        client = Client()      
        course1 = Course.objects.create(name = 'PyBursa', short_description = 'Web development')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PyBursa')
 
    def test_course_lesson(self):
        client = Client()      
        course1 = Course.objects.create(name = 'PyBursa', short_description = 'Web development')
        course2 = Course.objects.create(name = 'Django', short_description = 'Short description Django')
        lesson1 = Lesson.objects.create(subject = 'First', description = 'Short description First', order = 1, course = course1)
        #lesson2 = Lesson.objects.create(subject = 'Second', description = 'Short description Second', order = 2, course = course1)        
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'First')
        response = client.get('/courses/2/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'First')

    def test_course_coach(self):
        client = Client()
        user1 = User.objects.create(username = 'Ivan', first_name = 'Vanya')
        user2 = User.objects.create(username = 'Petro', first_name = 'Petya')
        coach1 = Coach.objects.create(user = user1, date_of_birth = '1990-02-18')
        coach2 = Coach.objects.create(user = user2, date_of_birth = '1980-11-23')      
        course1 = Course.objects.create(name = 'PyBursa', short_description = 'Web development', coach = coach2, assistant = coach2)
        course2 = Course.objects.create(name = 'Django', short_description = 'Short description Django', coach = coach1, assistant = coach1)
     
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        #self.assertIn(, 'Petro')
        self.assertContains(response, 'Petya')
        self.assertNotContains(response, 'Vanya')

        response = client.get('/courses/2/')
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(course2.coach.pk, 1)
        self.assertContains(response, 'Vanya')
        self.assertNotContains(response, 'Petya')

    def test_course_detail(self):
        client = Client()
        course1 = Course.objects.create(name = 'PyBursa', short_description = 'Web development')
        response = client.get('/courses/1/')
        self.assertTemplateUsed(response, 'courses/detail.html')# проверка вызова шаблона
        self.assertNotContains(response, 'Web')
        self.assertContains(response, 'PyBursa')

    def test_lesson_add_template(self):
        client = Client()
        response = client.get('/courses/1/add_lesson/')
        self.assertTemplateUsed(response, 'courses/add_lesson.html')# проверка вызова шаблона



