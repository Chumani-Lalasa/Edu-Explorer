from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course, Module, Content, ContentProgress

class ContentTrackingTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.course = Course.objects.create(title='Test Course', description='Course Description', instructor=self.user)
        self.module = Module.objects.create(course=self.course, title='Test Module', description='Module Description', order=1)
        self.content = Content.objects.create(module=self.module, content_type='video', text='Video Content Description', order=1)
        self.client.login(username='testuser', password='password')

    def test_mark_content_as_viewed(self):
        url = reverse('content-progress', kwargs={'content_id': self.content.id})
        data = {
            'viewed': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(ContentProgress.objects.filter(user=self.user, content=self.content, viewed=True).exists())
    
    def test_create_content(self):
        url = reverse('content-create')
        data = {
            'title': 'New Content',
            'module': self.module.id,
            'description': 'Content Description'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 