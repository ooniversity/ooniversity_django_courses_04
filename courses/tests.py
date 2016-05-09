from django.test import TestCase, Client
from django.contrib.auth.models import User

from coaches.models import Coach
from courses.models import Course, Lesson


def new_course_lead(name):
    return Coach.objects.create(
        user=User.objects.create_user(
            username = name,
            first_name = name,
            last_name = name,
            password = 'password123',
            email = name + '@example.com',
        ),
        date_of_birth = '1980-01-01',
        gender='M',
        phone='12345678',
        address = 'address',
        skype = name + '.skype',
        description = 'description',
    )


def new_course(name):
    course = Course.objects.create(
        name = name,
        short_description = 'short description for course',
        description = 'description for course',
        coach = new_course_lead('courseLead'),
        assistant = new_course_lead('courseAssistant'),
    )
    for i in range(3):
        Lesson.objects.create(
            subject='lesson ' + str(i),
            description = 'description for lesson ' + str(i),
            course = course,
            order = i,
    )


class CoursesListTest(TestCase):

    def test_statuscode(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_title(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'MyBursa | Main')

    def test_template(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_new_course_statuscode(self):
        client = Client()
        new_course('course 1')
        response = client.get('/')
        self.assertTrue(response.status_code == 200)

    def test_new_course_content(self):
        client = Client()
        new_course('course content')
        response = client.get('/')
        self.assertContains(response, 'Course Content')



class CoursesDetailTest(TestCase):

    def test_statuscode(self):
        client = Client()
        new_course('course 1')
        response = client.get('/courses/1', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_title(self):
        client = Client()
        new_course('course 1')
        response = client.get('/courses/1', follow=True)
        self.assertContains(response, 'MyBursa | Course  Detail')

    def test_template(self):
        client = Client()
        new_course('course 1')
        response = client.get('/courses/1', follow=True)
        self.assertTemplateUsed(response, 'courses/detail.html')

    def test_new_course_statuscode(self):
        client = Client()
        new_course('course 1')
        response = client.get('/courses/1', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_new_course_content(self):
        client = Client()
        new_course('course content')
        response = client.get('/courses/1', follow=True)
        self.assertContains(response, 'course content')

    def test_new_course_coach_content(self):
        client = Client()
        new_course('course content')
        response = client.get('/courses/1', follow=True)
        self.assertContains(response, 'COURSELEAD')

    def test_new_course_lesson_content(self):
        client = Client()
        new_course('course content')
        response = client.get('/courses/1', follow=True)
        self.assertContains(response, 'lesson 1')
