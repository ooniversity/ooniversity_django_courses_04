from django.test import TestCase, Client
from courses.models import Course
from coaches.models import Coach
from django.contrib.auth.models import User
import datetime


def createDB():
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    coach = Coach.objects.create(user=user,
                                 date_of_birth=datetime.datetime(1999,9,9),
                                 gender="Male",
                                 phone="12345678",
                                 address="address",
                                 skype="skype",
                                 description="description")
    Course.objects.create(name="test_name",
                          short_description="test_short_description",
                          description="test_description",
                          coach=coach,
                          assistant=coach)


class CoursesListTest(TestCase):
    def setUp(self):
        createDB()

    client = Client()

    def test_get_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        response = self.client.get("/")
        self.assertEqual(len(response.context["courses"]), 1)

    def test_name(self):
        response = self.client.get("/")
        self.assertEqual(response.context["courses"][0].name, "test_name")

    def test_short_description(self):
        response = self.client.get("/")
        self.assertEqual(response.context["courses"][0].short_description, "test_short_description")

    def test_description(self):
        response = self.client.get("/")
        self.assertEqual(response.context["courses"][0].description, "test_description")


class CoursesDetailTest(TestCase):
    def setUp(self):
        createDB()

    client = Client()

    def test_get_page(self):
        response = self.client.get("/courses/1/")
        self.assertEqual(response.status_code, 200)

    def test_coach_name(self):
        response = self.client.get("/courses/1/")
        self.assertEqual(response.context["courses"].coach.user.username, 'john')

    def test_name(self):
        response = self.client.get("/courses/1/")
        self.assertEqual(response.context["courses"].name, "test_name")

    def test_coach_description(self):
        response = self.client.get("/courses/1/")
        self.assertEqual(response.context["courses"].coach.description, "description")

    def test_description(self):
        response = self.client.get("/courses/1/")
        self.assertEqual(response.context["courses"].description, "test_description")

