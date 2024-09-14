from django.utils import timezone
from .models import Notification, Content, ContentProgress, Quiz, QuizProgress

def check_incomplete_content(user):
    incomplete_content = Content.objects.exclude(
        contentprogress__user=user, contentprogress__viewed=True
    )
    for content in incomplete_content:
        message = f"You have not completed the content: {content.text}"
        Notification.objects.create(user=user, message=message)

def check_incomplete_quizzes(user):
    incomplete_quizzes = Quiz.objects.exclude(
        quizprogress__user=user, quizprogress__completed=True
    )
    for quiz in incomplete_quizzes:
        message = f"You have not completed the quiz: {quiz.title}"
        Notification.objects.create(user=user, message=message)

