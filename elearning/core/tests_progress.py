from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Course, Quiz, CourseProgress, QuizProgress, Question, QuestionAnswer, Module, Content, ContentProgress
from django.urls import reverse

class CourseProgressTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.course = Course.objects.create(title='Test Course', description='Course Description', instructor=self.user)
        self.client.login(username='testuser', password='password')
        self.progress = CourseProgress.objects.create(user=self.user, course=self.course)
        self.module = Module.objects.create(course=self.course, title='Test Module', description='Module Description', order=1)
        self.content = Content.objects.create(module=self.module, content_type='video', text='Video Content Description', order=1)

    def test_get_course_progress(self):
        url = reverse('course-progress', kwargs={'course_id': self.course.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['course'], self.course.id)
        self.assertIn('completion_status', response.data)

    def test_post_course_progress(self):
        url = reverse('course-progress', kwargs={'course_id': self.course.id})
        data = {'completed_modules': [self.module.id], 'completion_status': True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(CourseProgress.objects.filter(user=self.user, course=self.course, completion_status=True).exists())

    def test_course_progress_unauthenticated(self):
        self.client.logout()
        url = reverse('course-progress', kwargs={'course_id': self.course.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_content_tracking(self):
        url = reverse('content-progress', kwargs={'content_id': self.content.id})
        data = {'viewed': True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(ContentProgress.objects.filter(user=self.user, content=self.content, viewed=True).exists())

class QuizProgressTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.course = Course.objects.create(title='Test Course', description='Course Description', instructor=self.user)
        self.quiz = Quiz.objects.create(title='Test Quiz', description='Quiz Description', course=self.course)
        self.client.login(username='testuser', password='password')
        self.progress = QuizProgress.objects.create(user=self.user, quiz=self.quiz)

    def test_get_quiz_progress(self):
        url = reverse('quiz-progress', kwargs={'quiz_id': self.quiz.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quiz'], self.quiz.id)
        self.assertIn('score', response.data)

    def test_post_quiz_progress(self):
        url = reverse('quiz-progress', kwargs={'quiz_id': self.quiz.id})
        data = {'score': 80, 'completed': True, 'completed_at': '2024-08-22T12:00:00Z'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['score'], 80)
        self.assertTrue(QuizProgress.objects.filter(user=self.user, quiz=self.quiz, score=80).exists())

    def test_quiz_progress_unauthenticated(self):
        self.client.logout()
        url = reverse('quiz-progress', kwargs={'quiz_id': self.quiz.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class QuestionAnswerTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.course = Course.objects.create(title='Test Course', description='Course Description', instructor=self.user)
        self.quiz = Quiz.objects.create(title='Test Quiz', description='Quiz Description', course=self.course)
        self.question = Question.objects.create(text='What is 2 + 2?', correct_answer='4', quiz=self.quiz)
        self.client.login(username='testuser', password='password')

    def test_post_question_answer(self):
        url = reverse('question-answer', kwargs={'question_id': self.question.id})
        data = {'selected_answer': '4'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['is_correct'])

    def test_question_answer_unauthenticated(self):
        self.client.logout()
        url = reverse('question-answer', kwargs={'question_id': self.question.id})
        data = {'selected_answer': '4'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class IncompleteContentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.course = Course.objects.create(title='Test Course', description='Course Description', instructor=self.user)
        self.module = Module.objects.create(course=self.course, title='Test Module', description='Module Description', order=1)
        self.content_1 = Content.objects.create(module=self.module, content_type='video', text='Content 1', order=1)
        self.content_2 = Content.objects.create(module=self.module, content_type='video', text='Content 2', order=2)
        self.client.login(username='testuser', password='password')

    def test_incomplete_content(self):
        # Simulate that only content_1 is completed
        ContentProgress.objects.create(user=self.user, content=self.content_1, viewed=True)
        
        url = reverse('course-progress', kwargs={'course_id': self.course.id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('incomplete_content', response.data)
        incomplete_content_ids = [content['id'] for content in response.data['incomplete_content']]
        self.assertIn(self.content_2.id, incomplete_content_ids)  # content_2 should be incomplete
        self.assertNotIn(self.content_1.id, incomplete_content_ids)  # content_1 should not be incomplete

class IncompleteQuizTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.course = Course.objects.create(title='Test Course', description='Course Description', instructor=self.user)
        self.quiz_1 = Quiz.objects.create(title='Quiz 1', description='First quiz', course=self.course)
        self.quiz_2 = Quiz.objects.create(title='Quiz 2', description='Second quiz', course=self.course)
        self.client.login(username='testuser', password='password')

    def test_incomplete_quizzes(self):
        # Simulate that quiz_1 is completed
        QuizProgress.objects.create(user=self.user, quiz=self.quiz_1, score=100, completed=True)
        
        url = reverse('course-progress', kwargs={'course_id': self.course.id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('incomplete_quizzes', response.data)
        incomplete_quiz_ids = [quiz['id'] for quiz in response.data['incomplete_quizzes']]
        self.assertIn(self.quiz_2.id, incomplete_quiz_ids)  # quiz_2 should be incomplete
        self.assertNotIn(self.quiz_1.id, incomplete_quiz_ids)  # quiz_1 should not be incomplete




