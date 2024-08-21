from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@example.com')
        self.course = Course.objects.create(name='Физра', description='беготня')
        self.lesson = Lesson.objects.create(name='Воллейбол', description='игра с мячом', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lessons_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('name'), self.lesson.name)

    def test_create_lesson(self):
        url = reverse("materials:lessons_create")
        data = {
            "name": "New test lesson",
            "description": "New test lesson description",
            "video_link": "https://www.youtube.com/watch?v=gomhMmutBd9",
            "course": self.course.pk
        }
        response = self.client.post(url, data)
        # self.assertEqual(
        #     response.status_code, status.HTTP_201_CREATED
        # )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

