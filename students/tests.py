from django.test import TestCase, Client
from courses.models import Course
from coaches.models import Coach
from students.models import Student
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
        course = Course.objects.create(name="test_course",
                                       short_description="test_short_description",
                                       description="test_description",
                                       coach=coach,
                                       assistant=coach)
        Student.objects.create(name="Test_name",
                               surname="Test_surname",
                               date_of_birth=datetime.datetime(1999,9,9),
                               email="test@mail.com",
                               phone="1234567",
                               address="test_address",
                               skype="test_skype")


class StudentsListTest(TestCase):
    def setUp(self):
        createDB()

    client = Client()

    def test_get_page(self):
        response = self.client.get("/students/")
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        response = self.client.get("/students/")
        self.assertEqual(len(response.context["object_list"]), 1)

    def test_name(self):
        response = self.client.get("/students/")
        self.assertEqual(response.context["object_list"][0].name, "Test_name")

    def test_address(self):
        response = self.client.get("/students/")
        self.assertEqual(response.context["object_list"][0].address, "test_address")

    def test_skype(self):
        response = self.client.get("/students/")
        self.assertEqual(response.context["object_list"][0].skype, "test_skype")


class StudentsDetailTest(TestCase):
    def setUp(self):
        createDB()

    client = Client()

    def test_get_page(self):
        response = self.client.get("/students/1/")
        self.assertEqual(response.status_code, 200)

    def test_surname(self):
        response = self.client.get("/students/1/")
        self.assertEqual(response.context["student"].surname, 'Test_surname')

    def test_name(self):
        response = self.client.get("/students/1/")
        self.assertEqual(response.context["student"].name, "Test_name")

    def test_address(self):
        response = self.client.get("/students/1/")
        self.assertEqual(response.context["student"].address, "test_address")

    def test_skype(self):
        response = self.client.get("/students/1/")
        self.assertEqual(response.context["student"].skype, "test_skype")

