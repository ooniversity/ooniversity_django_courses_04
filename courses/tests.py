from django.test import TestCase
from django.contrib.auth.models import User

from courses.models import Course
from coaches.models import Coach

# Create your tests here.
class CoursesListTest(TestCase):
    
    def setUp(self):
        for title in ["Python", "Java", "Ruby", "C#", "C++"]:
            Course.objects.create(
                name = title,
                short_description = "this is shoort test description",
                description = "this is long test description",
            )
    

    def test_response_number(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)


    def test_created_course(self):
        response = self.client.get('/')

        self.assertContains(response, "Java")


    def test_check_title(self):
        response = self.client.get('/')

        self.assertContains(response, "Welcome!")


    def test_pagination(self):
        response = self.client.get('/?page=5')

        self.assertEqual(response.status_code, 200)


    def test_list_url_active(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')


class CoursesDetailTest(TestCase):
    
    def setUp(self):
        Coach.objects.create(
            user=User.objects.create_user(
                username='coach_1',
                password='coach_1',
                email='coach_1@coach.com',
            ),
            date_of_birth='2001-01-07',
            gender='M',
            phone='1234657980',
            address='Test address',
            skype='test_skypr',
            description='Test description',
        )
        
        for title in ["Python", "Java", "Ruby", "C#", "C++"]:
            Course.objects.create(
                name = title,
                short_description = "this is shoort test description",
                description = "this is long test description",
                coach=Coach.objects.get(id=1),
                assistant=Coach.objects.get(id=1),
            )
    

    def test_response_number(self):
        for page in ['1', '2', '3', '4', '5']:
            response = self.client.get('/courses/%s/' % page)

            self.assertEqual(response.status_code, 200)


    def test_created_course(self):
        response = self.client.get('/courses/4/')

        self.assertContains(response, "C#")


    def test_check_title(self):
        response = self.client.get('/courses/2/')

        self.assertContains(response, "Java")


    def test_wrong_course(self):
        response = self.client.get('/courses/7/')

        self.assertEqual(response.status_code, 404)


    def test_list_url_active(self):
        response = self.client.get('/courses/1/')
        self.assertTemplateUsed(response, 'courses/detail.html')