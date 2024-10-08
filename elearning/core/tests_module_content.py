# tests_module_content.py
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course, Module, Content, ContentProgress

class ModuleContentTests(APITestCase):

    def setUp(self):
        # Create a test user and log in
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create a course and module
        self.course = Course.objects.create(title='Test Course', description='Course Description', instructor=self.user)
        self.module = Module.objects.create(course=self.course, title='Test Module', description='Module Description', order=1)

        # Create initial content
        self.content = Content.objects.create(module = self.module, content_type='article', order=1)

    def test_create_module(self):
        url = reverse('module-create', kwargs={'course_id': self.course.id})
        data = {'title': 'New Module', 'description': 'New Module Description', 'order': 2}
        response = self.client.post(url, data, format='json')
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Module.objects.count(), 2)
        self.assertEqual(Module.objects.last().title, 'New Module')

    def test_update_module(self):
        url = reverse('module-update', kwargs={'pk': self.module.id})
        data = {'title': 'Updated Module', 'description': 'Updated Module Description', 'order': 1}
        response = self.client.put(url, data, format='json')

        print("Response Data: ",response.data)
        print("Response status Code:", response.status_code)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.module.refresh_from_db()
        self.assertEqual(self.module.title, 'Updated Module')
        self.assertEqual(self.module.description, 'Updated Module Description')
        self.assertEqual(self.module.order, 1)

    def test_delete_module(self):
        url = reverse('module-delete', kwargs={'pk': self.module.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Module.objects.count(), 0)

    def test_create_content(self):
        # The Content table starts empty before the test
        Content.objects.all().delete()

        url = reverse('content-create', args=[self.module.id])
        data = {'content_type': 'video', 'text': 'New Content Description', 'module': self.module.id, 'order': 1}
        response = self.client.post(url, data, format='json')

        print(response.data)  # Print response data to debug
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Content.objects.count(), 1)
        self.assertEqual(Content.objects.first().text, 'New Content Description')

    def test_update_content(self):
        content = Content.objects.create(module=self.module, content_type='video', text='Old Content Description', order=1)
        url = reverse('content-update', kwargs={'pk': content.id})
        data = {'content_type': 'video', 'text': 'Updated Content Description', 'order': 1}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content.refresh_from_db()
        self.assertEqual(content.text, 'Updated Content Description')

    def test_delete_content(self):
        # Create the content to be deleted
        content_to_delete = Content.objects.create(module=self.module, content_type='video', text='Content to Delete', order=2)
        
        # Assert there is 2 content items
        self.assertEqual(Content.objects.count(), 2)

        # Prepare the delete request
        url = reverse('content-delete', kwargs={'pk': content_to_delete.id})
        response = self.client.delete(url)

        # Output
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)

        # Assert deletion was successful
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Content.objects.count(), 1)

    def test_mark_content_as_viewed(self):
        # Make a POST request to mark the content as viewed
        url = reverse('content-progress', kwargs={'content_id': self.content.id})
        data = {'viewed': True}
        
        response = self.client.post(url, data, format='json')
        
        # Check if the response status is OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify that ContentProgress for the user and content is marked as viewed
        self.assertTrue(ContentProgress.objects.filter(user=self.user, content=self.content, viewed=True).exists())
