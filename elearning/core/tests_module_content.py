from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course, Module, Content

class ModuleContentTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.course = Course.objects.create(title='Test Course', description='Course Description', instructor=self.user)
        self.module = Module.objects.create(course=self.course, title='Test Module', description='Module Description', order=1)

    def test_create_module(self):
        url = reverse('module-create', kwargs={'course_id': self.course.id})
        data = {
            'title': 'New Module',
            'description': 'New Module Description',
            'order': 2
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Module.objects.count(), 2)
        self.assertEqual(Module.objects.last().title, 'New Module')

    def test_update_module(self):
        url = reverse('module-update', kwargs={'pk': self.module.id})
        data = {
            'title': 'Updated Module',
            'description': 'Updated Module Description',
            'order': 1
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.module.refresh_from_db()
        self.assertEqual(self.module.title, 'Updated Module')

    def test_delete_module(self):
        url = reverse('module-delete', kwargs={'pk': self.module.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Module.objects.count(), 0)

    def test_create_content(self):
        url = reverse('content-create', kwargs={'module_id': self.module.id})
        data = {
            'content_type': 'video',
            'text': 'Video Content Description',
            'order': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Content.objects.count(), 1)
        self.assertEqual(Content.objects.last().content_type, 'video')

    def test_update_content(self):
        content = Content.objects.create(module=self.module, content_type='article', text='Article Content', order=1)
        url = reverse('content-update', kwargs={'pk': content.id})
        data = {
            'content_type': 'file',
            'text': 'Updated Content',
            'order': 1
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content.refresh_from_db()
        self.assertEqual(content.content_type, 'file')
        self.assertEqual(content.text, 'Updated Content')

    def test_delete_content(self):
        content = Content.objects.create(module=self.module, content_type='quiz', text='Quiz Content', order=1)
        url = reverse('content-delete', kwargs={'pk': content.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Content.objects.count(), 0)

    def test_unauthorized_module_creation(self):
        self.client.logout()
        url = reverse('module-create', kwargs={'course_id': self.course.id})
        data = {
            'title': 'Unauthorized Module',
            'description': 'Unauthorized Description',
            'order': 3
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthorized_content_creation(self):
        self.client.logout()
        url = reverse('content-create', kwargs={'module_id': self.module.id})
        data = {
            'content_type': 'article',
            'text': 'Unauthorized Content',
            'order': 2
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
