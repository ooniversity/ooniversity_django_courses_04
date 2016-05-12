from django.core.urlresolvers import reverse
from django.test import TestCase

class StudentsListTest(TestCase):

    def get_response(self):
        return self.client.get(reverse('students:list_view'))

    def test_students_list_response(self):
        self.assertEqual(self.get_response().status_code, 200)
