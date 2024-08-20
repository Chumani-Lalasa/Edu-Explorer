from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Course
from django.urls import reverse

# Create your tests here.
class CourseTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
    
    def test_create_course(self):
        url = reverse('course-create')
        data = {'title' : 'Test course', 'description' : 'A test course'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'].lower(), 'test course')
    
    def test_update_course(self):
        # create a course to update
        course = Course.objects.create(title='Original Title', description='Original Description', instructor=self.user)
        url = reverse('course-update', kwargs={'pk': course.pk})
        data = {'title': 'Updated Title', 'description' : 'Updated Description'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Title')

    def test_delete_course(self):
        course = Course.objects.create(title='Course to Delete', description='Will be deleted', instructor=self.user)
        url = reverse('course-delete', kwargs={'pk':course.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Course.objects.filter(pk=course.pk).exists())