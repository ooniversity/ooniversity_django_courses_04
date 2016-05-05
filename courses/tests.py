# -*- coding: utf-8 -*-
from django.test import TestCase
from courses.models import Course
from django.test import Client


class CoursesListTest(TestCase):
    def test_list(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

class CoursesDetailTest(TestCase):
    def test_detail_course(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)




'''
    def test_content(self):
        course1 = Course.objects.create(
            name = 'PythonBase',
            short_description = 'Основы программирования Python')
        course2 = Course.objects.create(
            name = 'PythonBase',
            short_description = 'Основы программирования Python')
        course3 = Course.objects.create(
            name = 'PythonBase',
            short_description = 'Основы программирования Python')
        client = Client()
        response = client.get('/')
        self.assertEqual(Course.objects.all(), 6)

        course2 = Course.objects.create(
            name = 'Python Base',
            short_description = 'Python Base Course')
        client = Client()
        response = client.get('/')
        self.assertEqual(Course.objects.all(), 1)
'''





'''
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