from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Course, Quiz, Question, Answer, User, Module, Content, ContentProgress, QuizProgress, CourseProgress
from django.urls import reverse
from .utils import check_incomplete_quizzes
from core.models import CourseProgress, Notification

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
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['course'], self.course.id)
        self.assertIn('completion_status', response.data['progress'])

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
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_view_content_tracking(self):
        url = reverse('content-progress', kwargs={'content_id': self.content.id})
        data = {'viewed': True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(ContentProgress.objects.filter(user=self.user, content=self.content, viewed=True).exists())

class QuestionAnswerTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.course = Course.objects.create(title='Test Course', description='Course Description', instructor=self.user)
        self.quiz = Quiz.objects.create(title='Test Quiz', description='Quiz Description', course=self.course)

        # create the question instance using the answer instance
        self.question = Question.objects.create(
            text='What is 2 + 2?', 
            correct_answer=None, 
            quiz=self.quiz
        )

        # create an answer instance and link it to the question
        self.correct_answer = Answer.objects.create(text='4', question = self.question, is_correct = True)

        # Update the question's correct_answer field to be the correct Answer instance
        self.question.correct_answer = self.correct_answer
        self.question.save()

        # Log in the test user
        self.client.login(username='testuser', password='password')

    def test_post_question_answer(self):
        url = reverse('question-answer', kwargs={'question_id': self.question.id})
        data = {'selected_answer': self.correct_answer.id}
        response = self.client.post(url, data, format='json')

        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['is_correct'], "The answer should be correct")

    def test_question_answer_unauthenticated(self):
        self.client.logout()
        url = reverse('question-answer', kwargs={'question_id': self.question.id})
        data = {'selected_answer': '4'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class IncompleteContentTests(TestCase):
    def setUp(self):
        # Create a test user to act as the instructor
        self.instructor_user = User.objects.create_user(username='instructor_user', password='password')

        # Create a course with the instructor
        self.course = Course.objects.create(
            name='Test Course',
            title='Test Course Title',
            description='This is a test course description.',
            duration=60,  # Example duration in minutes
            instructor=self.instructor_user  # Setting the instructor
        )
        
        # Create a module for the course
        self.module = Module.objects.create(title='Test Module', course=self.course)

        # Create some content for the module
        self.content_1 = Content.objects.create(content_type='article', module=self.module, text='Content 1', order=1)
        self.content_2 = Content.objects.create(content_type='quiz', module=self.module, text='Content 2', order=2)

        # Create course progress for the test user
        self.test_user = User.objects.create_user(username='testuser', password='password')
        self.course_progress = CourseProgress.objects.create(user=self.test_user, course=self.course)

        # Mark content_1 as completed
        self.course_progress.completed_content.add(self.content_1)
        self.course_progress.save()

        self.client = APIClient()
        self.client.login(username = 'testuser', password = 'password')

    def test_incomplete_content(self):
        response = self.client.get(f'/api/progress/course/{self.course.id}/')
        
        # Print the response data for debugging
        print(response.data)

        # Ensure 'incomplete_content' is in the response data
        self.assertIn('incomplete_content', response.data, "Response does not contain 'incomplete_content'")

        incomplete_content_ids = [content['id'] for content in response.data['incomplete_content']]
        print("Completed Content IDs:", list(self.course_progress.completed_content.values_list('id', flat=True)))

        self.assertNotIn(self.content_1.id, incomplete_content_ids, "Content 1 should be marked as completed")

class IncompleteQuizTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
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
        # Create QuizProgress for the user, marking it as incomplete (completed=False)
        self.quiz_progress = QuizProgress.objects.create(
            user = self.user,
            quiz = self.quiz,
            completed=False,
            score=0
        )

    def test_incomplete_quizzes(self):

        check_incomplete_quizzes(self.user)
        
        notification = Notification.objects.filter(
            user=self.user, message=f"You have not completed the quiz: {self.quiz.title}"
        ).first()

        self.assertIsNotNone(notification)
        self.assertEqual(notification.message, f"You have not completed the quiz: {self.quiz.title}")
