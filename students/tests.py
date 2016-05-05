# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from students.models import Student


class StudentsListTest(TestCase):
    def test_list_statuscode(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

class StudentsDetailTest(TestCase):
    def test_detail_create(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)