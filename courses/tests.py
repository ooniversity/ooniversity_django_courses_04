# -*- coding: utf-8 -*-
from django.test import TestCase
from courses.models import Course
from django.test import Client


items = {
    'course1': {
        'name': 'PythonBase',
        'short_description': 'Основы программирования Python',
    }
}

def create_item(item):
    return Course.objects.create(**item)

def create_items():
    for item in items.keys():
        create_item(items[item])


class CoursesListTest(TestCase):

    def test_course_create(self):
        create_items()
        self.assertEqual(Course.objects.all().count(), 1)
    def test_index(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)
    def test_Course_TST(self):
        client = Client()
        response = client.get('courses/1/')
        self.assertEqual(response.status_code, 200)
#        self.assertContains(response, "Python Base")

#        self.assertContains(response, "Python Base", status_code=200)






'''
from django.test import Client


items = {
    'course1': {
        'name': 'Python Base',
        'short_description': 'Основы программирования Python',
    }}

def create_item(item):
    return Course.objects.create(**item)

def create_items():
    for item in items.keys():
        create_item(items[item])

class CoursesListTest(TestCase):
    def test_course_create(self):
        create_items()
        self.assertEqual(Course.objects.all().count(), 2)
        client = Client()
        response = Client.get('/courses/')
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Course1", status_code=200)
        self.assertContains(response, "Course2", status_code=200)

#       course1 = Course.objects.create(
#                                       name='Python Base',
#                                       #short_description="Основы программирования Python"
#                                       )
#       self.assertEqual(Course.object.all().count(), 1)
#   def test_pages(self):
#       client = Client()
#
#       response = client.get('/courses/')
#       self.assertEqual(response.status_code, 404)
##
#       response = client.get('/courses/1/')
#       self.assertEqual(response.status_code, 200)
'''