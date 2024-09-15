from django.utils import timezone
from .models import Notification, Content, ContentProgress, Quiz, QuizProgress

def check_incomplete_content(user, course_id):
   incomplete_quizzes = Quiz.objects.exclude(
        quizprogress__user=user, quizprogress__completed=True
    )
   for quiz in incomplete_quizzes:
       message = f"You have not completed the quiz: {quiz.title}"
       Notification.objects.create(user = user, message = message)
    # pass

def check_incomplete_quizzes(user):
    incomplete_quizzes = Quiz.objects.filter(
        quizprogress__user=user, quizprogress__completed=False
    ).distinct()
    
    for quiz in incomplete_quizzes:
        message = f"You have not completed the quiz: {quiz.title}"
        Notification.objects.create(user=user, message=message)

