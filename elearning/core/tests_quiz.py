from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Course, Quiz, Question, QuizProgress, QuestionAnswer, Answer

class QuizManagementTests(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a course with the user as the instructor
        self.course = Course.objects.create(
            name='Test Course',
            title='Test Course Title',
            description='Test Course Description',
            instructor=self.user
        )
        
        # Create a quiz and related objects
        self.quiz = Quiz.objects.create(
            title='Test Quiz',
            description='A test quiz',
            course=self.course  # Ensure this ID is valid
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
        
        self.url = reverse('evaluatequiz-list')  # Adjust if necessary
    
    def test_create_quiz(self):
        url = reverse('quiz-list')  # Adjust if the URL name is different
        data = {
            'title': 'New Quiz',
            'description': 'New Quiz Description',
            'course': self.course.id  # Ensure this ID is valid
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Quiz.objects.count(), 2)  # Assuming 1 quiz was created

    def test_retrieve_quiz(self):
        url = reverse('quiz-detail', args=[self.quiz.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Quiz')

    def test_update_quiz(self):
        url = reverse('quiz-detail', args=[self.quiz.id])  # Adjust if necessary
        data = {
            'title': 'Updated Quiz Title',
            'description': 'Updated description'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.quiz.refresh_from_db()
        self.assertEqual(self.quiz.title, 'Updated Quiz Title')

    def test_delete_quiz(self):
        url = reverse('quiz-detail', args=[self.quiz.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Quiz.objects.count(), 0)

    def test_evaluate_quiz(self):
        url = reverse('evaluate-quiz', kwargs={'pk':4})  # Adjust if necessary
        data = {
            'answers': [
                {'question_id': self.question.id, 'answer_id': self.correct_answer.id},
                # {'question_id': self.question.id, 'selected_answer': self.wrong_answer.id}
            ]
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['score'], 1)  # Adjust based on expected result
        self.assertEqual(QuizProgress.objects.filter(quiz=self.quiz, user=self.user).count(), 1)

    def test_create_progress(self):
        url = reverse('quiz-progress', kwargs={'quiz_id': self.quiz.id})
        data = {
            'score': 5,
            'completed': True,
            'completed_at': '2024-09-05T10:00:00Z'
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(QuizProgress.objects.count(), 1)