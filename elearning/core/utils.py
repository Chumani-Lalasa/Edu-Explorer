from django.utils import timezone
from .models import Notification, Content, ContentProgress, Quiz, QuizProgress

def check_incomplete_content(user, course_id):
    # Fetch incomplete quizzes related to the course
    incomplete_quizzes = Quiz.objects.filter(
        course_id=course_id
    ).exclude(progress__user=user, progress__completed=True)

    print(f"Incomplete quizzes for course {course_id} and user {user.username}: {[quiz.title for quiz in incomplete_quizzes]}")

    # Fetch incomplete content (e.g., video, text) that the user has not viewed
    incomplete_content = Content.objects.filter(
        module__course_id=course_id
    ).exclude(progress__user=user, progress__viewed=True)

    print(f"Incomplete content for course {course_id} and user {user.username}: {[content.text for content in incomplete_content]}")

    incomplete_content_list = []

    # Notify user about incomplete quizzes
    for quiz in incomplete_quizzes:
        message = f"You have not completed the quiz: {quiz.title}"
        if not Notification.objects.filter(user=user, message=message).exists():
            Notification.objects.create(user=user, message=message)
        
        incomplete_content_list.append({'id': quiz.id, 'title': quiz.title})

    # Notify user about incomplete content (videos, text, etc.)
    for content in incomplete_content:
        message = f"You have not viewed the content: {content.text}"
        if not Notification.objects.filter(user=user, message=message).exists():
            Notification.objects.create(user=user, message=message)
        
        incomplete_content_list.append({'id': content.id, 'title': content.text})

    return incomplete_content_list


def check_incomplete_quizzes(user):
    # incomplete_quizzes = Quiz.objects.filter(
    #     progress__user = user,
    #     progress__completed=False
    # ).distinct()
    incomplete_quizzes = QuizProgress.get_incomplete_quizzes(user)

    for quiz in incomplete_quizzes:
        message = f"You have not completed the quiz: {quiz.title}"

        if not Notification.objects.filter(user = user, message = message).exists():
            Notification.objects.create(user=user, message=message)

