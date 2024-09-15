from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Course, Quiz, Question, QuizProgress, Answer

class QuizManagementTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            name='Test Course',
            title='Test Course Title',
            description='Test Course Description',
            instructor=self.user
        )
        self.quiz = Quiz.objects.create(
            title='Test Quiz',
            description='A test quiz',
            course=self.course
        )
        self.question = Question.objects.create(
            quiz=self.quiz,
            text='Test Question'
        )
        self.correct_answer = Answer.objects.create(
            question=self.question,
            text='Correct Answer',
            is_correct=True
        )
        self.wrong_answer = Answer.objects.create(
            question=self.question,
            text='Wrong Answer',
            is_correct=False
        )
        self.question.correct_answer = self.correct_answer
        self.question.save()

        self.quiz_url = reverse('quiz-list')
        self.quiz_detail_url = reverse('quiz-detail', args=[self.quiz.id])
        self.evaluate_quiz_url = reverse('evaluate-quiz', kwargs={'pk': self.quiz.id})
        self.create_progress_url = reverse('quiz-progress', kwargs={'quiz_id': self.quiz.id})

        # Create initial QuizProgress for testing progress retrieval
        self.quiz_progress = QuizProgress.objects.create(
            quiz=self.quiz,
            user=self.user,
            score=5,
            completed=True,
            completed_at='2024-09-05T10:00:00Z'
        )

    def test_create_quiz(self):
        data = {
            'title': 'New Quiz',
            'description': 'New Quiz Description',
            'course': self.course.id
        }
        response = self.client.post(self.quiz_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Quiz.objects.count(), 2)

    def test_retrieve_quiz(self):
        response = self.client.get(self.quiz_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Quiz')

    def test_update_quiz(self):
        data = {
            'title': 'Updated Quiz Title',
            'description': 'Updated description',
            'course': self.course.id
        }
        response = self.client.put(self.quiz_detail_url, data, format='json')
        print("Response Status Code:", response.status_code)
        print("Response Content:", response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.quiz.refresh_from_db()
        self.assertEqual(self.quiz.title, 'Updated Quiz Title')

    def test_delete_quiz(self):
        response = self.client.delete(self.quiz_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Quiz.objects.count(), 0)

    def test_evaluate_quiz(self):
        data = {
            'answers': [
                {'question_id': self.question.id, 'answer_id': self.correct_answer.id}
            ]
        }
        response = self.client.post(self.evaluate_quiz_url, data, format='json')
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('score', response.data)
        self.assertEqual(response.data['score'], 1.0)
        self.assertEqual(QuizProgress.objects.filter(quiz=self.quiz, user=self.user).count(), 1)

    def test_create_progress(self):
        data = {
            'score': 5,
            'completed': True,
            'completed_at': '2024-09-05T10:00:00Z'
        }
        response = self.client.post(self.create_progress_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(QuizProgress.objects.count(), 2)

    def test_get_quiz_progress(self):
        url = reverse('quiz-progress', kwargs={'quiz_id': self.quiz.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['progress']['quiz'], self.quiz.id)

    def test_quiz_progress_unauthenticated(self):
        url = reverse('quiz-progress', kwargs={'quiz_id': self.quiz.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
