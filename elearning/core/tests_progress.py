from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Course, Quiz, CourseProgress, QuizProgress, Question, QuestionAnswer
from django.urls import reverse

class CourseProgressTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.course = Course.objects.create(title='Test Course', description='Course Description', instructor = self.user)
        self.client.login(username='testuser', password='password')

    def test_get_course_progress(self):
        # Create progress entry for course
        CourseProgress.objects.create(user=self.user, course=self.course)
        url = reverse('course-progress', kwargs={'course_id' : self.course.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['course'], self.course.id)

    def test_post_course_progress(self):
        url = reverse('course-progress', kwargs={'course_id' : self.course.id})
        data = {
            'completed_modules':[],
            'completion_status': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['completion_status'], True)

# Quiz Progress Tests
class QuizPorgressTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.quiz = Quiz.objects.create(title='Test Quiz', description = 'Quiz Description', course = Course.objects.create(title='Test Course', description = 'Course Description', instructor = self.user))
        self.client.login(username = 'testuser', password='password')

    def test_get_quiz_progress(self):
        QuizProgress.objects.create(user = self.user, quiz = self.quiz)
        url = reverse('quiz-progress', kwargs={'quiz_id' : self.quiz.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quiz'], self.quiz.id)

    def test_post_quiz_progress(self):
        url = reverse('quiz-progress', kwargs={'quiz_id' : self.quiz.id})
        data = {
            'score' : 80,
            'completed' : True,
            'completed_at' : '2024-08-22T12:00:00Z'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['score'], 80)

class QuestionAnswerTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.question = Question.objects.create(text="What is 2 + 2?", correct_answer = '4', quiz = Quiz.objects.create(title='Test Quiz', description = 'Quiz Description', course = Course.objects.create(title='Test Course', description='Course Description', instructor=self.user)))
        self.client.login(username='testuser', password='password')

    def test_post_question_answer(self):
        url = reverse('question-answer', kwargs={'question_id' : self.question.id})
        data = {
            'selected_answer' : '4'
        }
        response = self.client.post(url, data, format='json')

        print("Response status code:", response.status_code)
        print("Response data:", response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['is_correct'])
        self.assertIn('is_correct', response.data)

