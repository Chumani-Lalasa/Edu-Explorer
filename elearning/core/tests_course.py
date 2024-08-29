from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Course

class CourseManagementTests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a test course
        self.course = Course.objects.create(
            title='Test Course',
            description='Test description',
            duration=30,
            instructor=self.user
        )
        
        # Define URL endpoints
        self.course_create_url = '/api/courses/create/'
        self.course_update_url = f'/api/courses/{self.course.id}/update/'
        self.course_delete_url = f'/api/courses/{self.course.id}/delete/'

    def test_create_course(self):
        data = {
            'title': 'New Course',
            'description': 'New course description.',
            'duration': 45
        }
        response = self.client.post(self.course_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)
        self.assertEqual(Course.objects.get(id=response.data['id']).title, 'New Course')

    def test_update_course(self):
        data = {
            'title': 'Updated Course Title',
            'description': 'Updated course description.',
            'duration': 40
        }
        response = self.client.put(self.course_update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.course.refresh_from_db()
        self.assertEqual(self.course.title, 'Updated Course Title')

    def test_delete_course(self):
        response = self.client.delete(self.course_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)
