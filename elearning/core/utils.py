from django.utils import timezone
from .models import Notification, Content, ContentProgress, Quiz, QuizProgress

def check_incomplete_content(user):
    content_list = Content.objects.all()
    for content in content_list:
        if not ContentProgress.objects.filter(user=user, content=content, viewed=True).exists():
            message = f"You have not completed the content: {content.text}"
            Notification.objects.create(user=user, message=message)

def check_incomplete_quizzes(user):
    quizzes = Quiz.objects.all()
    for quiz in quizzes:
        if not QuizProgress.objects.filter(user=user, quiz=quiz, completed=True).exists():
            message = f"You have not completed the quiz: {quiz.title}"
            Notification.objects.create(user=user, message=message)