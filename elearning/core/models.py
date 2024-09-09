from django.db import models
from django.contrib.auth.models import User
# from .models import Course, Quiz, Question
# from .models import Course, Quiz, Question

# Create your models here.

#User Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return self.user.username
    
#Course Model
class Course(models.Model):
    name = models.CharField(max_length=255, default='Unnamed Course')
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    instructor = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
# Module Model (New)
class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    description = models.TextField()
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.title} - {self.course.title}'
    
# Content Model (New)
class Content(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('video', 'Video'),
        ('article', 'Article'),
        ('quiz', 'Quiz'),
        ('file', 'File'),
    ]
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPE_CHOICES)  # e.g., "video", "article", "quiz"
    text = models.TextField(blank=True)  # Used for articles, descriptions, etc.
    file = models.FileField(upload_to='course_contents/', blank=True)  # Used for files like PDFs, images, etc.
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.content_type} - {self.module.title}'
    
# Lesson Model
class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveBigIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    
# Quiz Model
class Quiz(models.Model):
    course = models.ForeignKey(Course, related_name='quizzes', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# Question Model
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=50, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='medium')

    def __str__(self):
        return self.text
    
# Answer
class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers_list', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
# Model to track course progress
class CourseProgress(models.Model):
    user = models.ForeignKey(User, related_name='course_progress', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='progress', on_delete=models.CASCADE)
    completed_modules = models.ManyToManyField('Module', blank=True)
    completion_status = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.course.title}'

# Model to track quiz progress
class QuizProgress(models.Model):
    user = models.ForeignKey(User, related_name='quiz_progress', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name='progress', on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.quiz.title}'

# Model to track question answers
class QuestionAnswer(models.Model):
    user = models.ForeignKey(User, related_name='question_answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question_answers_list', on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.question.text}'

# Certificates Model
class Certificate(models.Model):
    user = models.ForeignKey(User, related_name='certificates', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='certificates', on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'Certificate for {self.user.username} - {self.course.title}'


