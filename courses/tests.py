# -*- coding: utf-8 -*-
import random

from django.test import TestCase
from coaches.models import Coach
from courses.models import Course, Lesson
from django.contrib.auth.models import User


class CoursesDetailTest(TestCase):
    fixtures = ['courses']

    def test_create_lesson(self):
        """ добавляю урок и проверяю наличие на странице наимен всех уроков этого курса """
        course = random.choice(Course.objects.all())        
        lessons = Lesson.objects.filter(course__id=course.id)
        les_id = lessons.count() + 1
        add_lesson(les_id, course.id)
        response = self.client.get('/courses/%d/'%course.id,{'page':les_id/3+1})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, Lesson.objects.filter(order=les_id)[0].subject)

    def test_coach_assistant(self):
        """ Коуч и ассистент """
        course = random.choice(Course.objects.all())
        response = self.client.get('/courses/%d/'%course.id)
        self.assertContains(response, course.coach.user.first_name)
        self.assertContains(response, course.assistant.user.first_name)

    def test_statuscode(self):
        """ создал новый курс и проверил статус ответа """        
        response = self.client.get('/courses/%d/'%create_course())
        self.assertEqual(response.status_code, 200)

    def test_edit_btn(self):
        """ переход по кнопке изменить """
        course = random.choice(Course.objects.all())
        response = self.client.get('/courses/%d/'%course.id)
        self.assertContains(response, '/courses/edit/%d/'%course.id)

    def test_coach_link(self):
        """ ссылка на коуча """
        course = random.choice(Course.objects.all())
        response = self.client.get('/coaches/{}/'.format(course.coach.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coaches/detail.html')

    def test_context(self):
        """ контекст """
        course = random.choice(Course.objects.all())
        response = self.client.get('/courses/{}/'.format(course.id))
        self.assertEqual(response.context['object'], course)


class CoursesListTest(TestCase):

    def test_templ_statuscode(self):
        """ шаблон и код ответа"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')	
        self.assertContains(response, 'Выбирай свой курс!')

    def test_list(self):
        """ список курсов на странице """
        response = self.client.get('/')
        for course in Course.objects.all():
            self.assertContains(response, course.name)

    def test_course_link(self):
        """ корректность ссылок на детальное описание и удаление """
        response = self.client.get('/')
        for course in Course.objects.all():
            self.assertContains(response, "/courses/{}/".format(course.id))
            self.assertContains(response, "/courses/remove/{}/".format(course.id))

    def test_active(self):
        """ активная ссылка """
        response = self.client.get('/')
        self.assertContains(response, """<li role="presentation" class=active><a href="/">Главная</a></li>""")


    def test_titles(self):
        """ заголовки """
        response = self.client.get('/')
        self.assertContains(response, u'ItBursa')
        self.assertContains(response, u'Description')


def create_course():
    course = Course.objects.create(
        name='course',
        short_description='s_descr',
        description='f_descr',
        coach=random.choice(Coach.objects.all()),
        assistant=random.choice(Coach.objects.all()),
    )
    return course.id


def add_lesson(lesson_id, course_id):
    Lesson.objects.create(
        subject = 'lesson_' + str(lesson_id),
        description = ' ',
        course = Course.objects.get(id=course_id),
        order = lesson_id,
    )



