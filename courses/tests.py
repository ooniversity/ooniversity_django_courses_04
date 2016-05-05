# -*- coding: utf-8 -*-
from django.test import TestCase
from courses.models import Course
from django.test import Client


class CoursesListTest(TestCase):
    def test_list(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_list_curs(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Курсы PyBursa')
    def test_list_Description(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Description')
    def test_list_url(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')
    def test_create_course(self):
        client = Client()
        Course.objects.create(
            name='course_1',
            short_description='В Этом Курсе Мы Сместили Акцент В Сторону Практики.',
            )
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
'''

    def test_course1_create(self):
        client = Client()
        course1 = Course.objects.create(
            name = 'PythonBase',
            short_description = 'Основы программирования Python')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Course.objects.all().count(), 1)
    def test_course2_create(self):
        client = Client()
        course1 = Course.objects.create(
            name = 'PythonExtended',
            short_description = 'Расширенный курс Python')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
    def test_course3_create(self):
        client = Client()
        course1 = Course.objects.create(
            name = 'Python Full',
            short_description = 'Полный курс Python')
        response = client.get('/courses/3/')
        self.assertEqual(response.status_code, 200)
    def test_course4_create(self):
        client = Client()
        course1 = Course.objects.create(
            name = 'Python Gold',
            short_description = 'Золотая серия курсов. Для избранных.')
        response = client.get('/courses/4/')
        self.assertEqual(response.status_code, 200)
'''

class CoursesDetailTest(TestCase):
    def test_detail_course(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

        course = Course.objects.create(
            name = 'Python Base',
            short_description = 'Основы программирования Python')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)




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