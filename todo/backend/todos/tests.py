from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Todo object for testing
        cls.todo = Todo.objects.create(title="Test Todo", body="This is a test todo item.")

    def test_model_content(self):
        self.assertEqual(self.todo.title, "Test Todo")
        self.assertEqual(self.todo.body, "This is a test todo item.")
        self.assertEqual(str(self.todo), "Test Todo")


class TodoAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title="Test Todo", body="This is a test todo item.")
        cls.list_url = reverse("todo_list")
        cls.detail_url = reverse("todo_detail", args=[cls.todo.id])

    def test_list_todos(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_detail_todo(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.todo.title)
        self.assertEqual(response.data["body"], self.todo.body)

    def test_detail_todo_not_found(self):
        response = self.client.get(reverse("todo_detail", args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)