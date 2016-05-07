# encoding: utf-8
import random

from django.test import TestCase
from students.models import Student
from courses.models import Course

def get_random_student():
    return random.choice(Student.objects.all())
    


class StudentsListTest(TestCase):
    fixtures = ['students.json']

    def test_get_students_list(self):
        """получаю список студентов из микстур"""
        std_lst = Student.objects.all()
        self.assertEqual(std_lst.count(), 6)

    def test_get_student_list_from_url(self):
        """ получаю список количество студентов на странице при пагинации = 2 """
        response = self.client.get('/students/')
        self.assertEqual(response.context['object_list'].count(), 2)

    def test_get_student_list_status_code(self):
        """ проверка кода ответа при запросе списка """
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
     
    def test_get_template(self):
        """ название шаблона """
        response = self.client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_course_id_students(self):
        """ студенты выбранного курса """
        course_id = 2
        response = self.client.get('/students/', {'course_id': course_id})
        std_filter = Student.objects.filter(courses__pk=course_id).all()      
        for std in response.context['object_list'].all():
            self.assertIn(std, std_filter)


class StudentsDetailTest(TestCase):
    fixtures = ['students.json']

    def test_student_name(self):
        """ соответствие имени и фамилии """
        std_id=get_random_student().id
        response = self.client.get('/students/%d/'%std_id)
        std_filter = Student.objects.get(pk=std_id)      
        self.assertContains(response, " ".join((std_filter.surname, std_filter.name)))

    def test_get_student_status_code(self):
        """ проверка кода ответа при запросе """
        response = self.client.get('/students/%d'%get_random_student().id)
        self.assertEqual(response.status_code, 301)

    def test_context(self):
        """ содержимое контекста """
        std_idd=get_random_student().id
        response = self.client.get('/students/%d/'%std_idd)
        self.assertEqual(response.context['object'], Student.objects.get(pk=std_idd))

    def test_get_template(self):
        """ название шаблона """
        std = get_random_student().id
        response = self.client.get('/students/%d/'%std)
        self.assertTemplateUsed(response, 'students/student_detail.html')

    def test_num_queries(self):
        with self.assertNumQueries(1):
            Student.objects.create(
                name = 'name',
                surname = "Surname",
                date_of_birth = "2000-01-07",
                email = "test@test.com",
                phone = "12345678",
                address = "Test address",
                skype = "test_skype",)            
    #def test_logger(self):
        #with self.assertLogs('logger', level='WARNING') as cm:
        #    logging.getLogger('logger').warning('Logger of students detail view warns you!')
        #self.assertEqual(cm.output, ['WARNING:logger:Logger of students detail view warns you!'])
