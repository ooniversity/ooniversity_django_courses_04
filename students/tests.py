from django.test import TestCase, Client
from students.models import Student
from  courses.models import Course
# Create your tests here.


class StudentsDetailTest(TestCase):

    def test_detail_work(self):
        client = Client()
        course1 = Course.objects.create(name='pybusra', short_description='just for test')
        student1 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student1.courses.add(course1)
        student1.save()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_st_course(self):
        client = Client()
        course1 = Course.objects.create(name='pybusra', short_description='just for test')
        student1 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student1.courses.add(course1)
        student1.save()
        response = client.get('/students/1/')
        self.assertContains(response, 'pybursa')

    def test_st_name(self):
        client = Client()
        course1 = Course.objects.create(name='pybusra', short_description='just for test')
        student1 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student1.courses.add(course1)
        student1.save()
        response = client.get('/students/1/')
        self.assertContains(response, 'zaika')

    def test_st_surname(self):
        client = Client()
        course1 = Course.objects.create(name='pybusra', short_description='just for test')
        student1 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student1.courses.add(course1)
        student1.save()
        response = client.get('/students/1/')
        self.assertContains(response, 'zaika')

    def test_st_skype(self):
        client = Client()
        course1 = Course.objects.create(name='pybusra', short_description='just for test')
        student1 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student1.courses.add(course1)
        student1.save()
        response = client.get('/students/1/')
        self.assertContains(response, 'asf')


class StudentsListTest(TestCase):

    def test_list_work(self):
        client = Client()
        course1 = Course.objects.create(name='pybusra', short_description='just for test')
        student1 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student1.courses.add(course1)
        student1.save()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_add_new_student(self):
        client = Client()
        course1 = Course.objects.create(name='pybusra', short_description='just for test')
        student1 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student1.courses.add(course1)
        student1.save()
        response = client.get('/students/add/')
        self.assertEqual(response.status_code, 200)

    def test_edit_student(self):
        client = Client()
        course1 = Course.objects.create(name='pybusra', short_description='just for test')
        student1 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student1.courses.add(course1)
        student1.save()
        response = client.get('/students/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'john')

    def test_remove_student(self):
        client = Client()
        course1 = Course.objects.create(name='pybusra', short_description='just for test')
        student1 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student1.courses.add(course1)
        student1.save()
        response = client.get('/students/remove/1/')
        self.assertEqual(response.status_code, 200)

    def test_pagination_student(self):
        client = Client()
        course1 = Course.objects.create(name='pybusra', short_description='just for test')
        student1 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student1.courses.add(course1)
        student1.save()
        student2 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student2.courses.add(course1)
        student2.save()
        student3 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student3.courses.add(course1)
        student3.save()
        response = client.get('/students/?page=2')
        self.assertEqual(response.status_code, 200)

    def test_detail_student_number_3(self):
        client = Client()
        course1 = Course.objects.create(name='pybusra', short_description='just for test')
        student1 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student1.courses.add(course1)
        student1.save()
        student2 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student2.courses.add(course1)
        student2.save()
        student3 = Student.objects.create(name='john', surname='zaika', date_of_birth='1994-04-13', skype='asf')
        student3.courses.add(course1)
        student3.save()
        response = client.get('/students/3/')
        self.assertEqual(response.status_code, 200)




