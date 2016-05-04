from django.test import TestCase

from students.models import Student

# Create your tests here.
class StudentsListTest(TestCase):
    
    def setUp(self):
        for name in ["Peter", "Ann", "Ivan", "George", "Ruslan"]:
            Student.objects.create(
                name = name,
                surname = "Surname",
                date_of_birth = "2000-01-07",
                email = "test@test.com",
                phone = "12345678",
                address = "Test address",
                skype = "test_skype",
            )
    

    def test_response_number(self):
        response = self.client.get('/students/')

        self.assertEqual(response.status_code, 200)


    def test_created_student(self):
        response = self.client.get('/students/')

        self.assertContains(response, "Peter")


    def test_check_title(self):
        response = self.client.get('/students/')

        self.assertContains(response, "Students list")


    def test_pagination(self):
        for page in ['2', '3', '2', '3', '3']:
            response = self.client.get('/students/?page=%s' % page)

            self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/students/?page=5')

        self.assertEqual(response.status_code, 404)

    def test_list_url_active(self):
        response = self.client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')


class StudentsDetailTest(TestCase):
    
    def setUp(self):
        for name in ["Peter", "Ann", "Ivan", "George", "Ruslan"]:
            Student.objects.create(
                name = name,
                surname = "Surname",
                date_of_birth = "2000-01-07",
                email = "test@test.com",
                phone = "12345678",
                address = "Test address",
                skype = "test_skype",
            )
    

    def test_response_number(self):
        for page in ['1', '2', '3', '4', '5']:
            response = self.client.get('/students/%s/' % page)

            self.assertEqual(response.status_code, 200)


    def test_created_student(self):
        response = self.client.get('/students/1/')

        self.assertContains(response, "Surname Peter")


    def test_check_title(self):
        response = self.client.get('/students/4/')

        self.assertContains(response, "Student details")


    def test_wrong_student(self):
        response = self.client.get('/students/8/')

        self.assertEqual(response.status_code, 404)

    def test_list_url_active(self):
        response = self.client.get('/students/2/')
        self.assertTemplateUsed(response, 'students/student_detail.html')