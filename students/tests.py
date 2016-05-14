from django.core.urlresolvers import reverse
from django.test import TestCase

from courses.models import Course
from students.models import Student


class StudentsListTest(TestCase):

    def setUp(self):
        create_student()

    def get_response(self):
        return self.client.get(reverse('students:list_view'))

    def get_student_add_response(self):
        return self.client.get(reverse('students:add'))

    def test_students_list_response(self):
        self.assertEqual(self.get_response().status_code, 200)

    def test_exist_link_student_add(self):
        self.assertEqual(self.get_student_add_response().status_code, 200)

    def test_student_template(self):
        self.assertTemplateUsed('students/list.html')

    def test_context_object_list(self):
        self.assertEqual(self.get_response().context['object_list'].count(), 1)

    def test_students_active_link(self):
        self.assertContains(self.get_response(), """<li class="active">
            <a href="/students/">Students</a></li>""")


class StudentsDetailTest(TestCase):

    def setUp(self):
        student = create_student()
        student.courses = [Course.objects.create(name=item) for item in ['Django', 'Spring', 'RoR']]

    def get_response(self):
        student = Student.objects.get(id=1)
        return self.client.get('/students/{}/'.format(student.id))

    def test_detail_response(self):
        self.assertEqual(self.get_response().status_code, 200)

    def test_student_detail_template(self):
        self.assertTemplateUsed(self.get_response(), 'students/student_detail.html')

    def test_student_unicode(self):
        student_context = self.get_response().context['student']
        self.assertEqual(Student.objects.get(id=1).__unicode__(), '{} {}'.format(student_context.name, student_context.surname))

    def test_students_true_link(self):
        self.assertContains(self.get_response(), """<a href="/students/">Students</a>""")

    def test_exist_course_detail_link(self):
        for key, value in {'1':'Django', '2':'Spring', '3':'RoR'}.items():
            self.assertContains(self.get_response(), """<a href="/courses/{}/">{}</a>""".format(key, value))

def create_student():
    return Student.objects.create(name='Sergej', surname='Viziryko', date_of_birth='1984-02-11', email='viziryak@gmail.com', phone='093942719', skype='kajzen')