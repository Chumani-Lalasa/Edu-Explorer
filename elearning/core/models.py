from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#User Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('instructor', 'Instructor'),
        ('student', 'Student'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
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
    pass
    
# Lesson Model
class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    module = models.ForeignKey(Module, related_name='lessons', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()                                                                                                                                                                                    
    order = models.PositiveBigIntegerField()
    progress = models.CharField(max_length=50, default=0)  # e.g., "completed", "incomplete"
    lesson_type = models.CharField(max_length=50, default='Standard')  # e.g., "video", "reading"
    category = models.CharField(max_length=50, default='General')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    pass
      
# Content Model (Connected to Lesson)
class Content(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('video', 'Video'),
        ('article', 'Article'),
        ('quiz', 'Quiz'),
        ('file', 'File'),
    ]
    lesson = models.ForeignKey(Lesson, related_name='contents', on_delete=models.CASCADE, null=True, blank=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, default='Untitled Content')
    description = models.TextField(default='No description provided')
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPE_CHOICES)  # e.g., "video", "article", "quiz"
    text = models.TextField(blank=True)  # Used for articles, descriptions, etc.
    file = models.FileField(upload_to='course_contents/', blank=True, null=True)  # Used for files like PDFs, images, etc.
    video_url = models.URLField(max_length=200,blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.content_type} - {self.lesson.title}' 

  
# Quiz Model
class Quiz(models.Model):
    content = models.OneToOneField(Content, related_name='quiz', on_delete=models.CASCADE, null=True, blank=True)  # Optional content field
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    pass
    

# Answer
# class Answer(models.Model):
#     question = models.ForeignKey('Question', related_name='answers', on_delete=models.CASCADE)
#     text = models.CharField(max_length=255)
#     is_correct = models.BooleanField(default=False)

#     def __str__(self):
#         return self.text
     
# # Question Model
# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     text = models.CharField(max_length=500)
#     correct_answer = models.ForeignKey(Answer, related_name='correct_for_question', on_delete=models.CASCADE, null=True, blank=True)
#     difficulty = models.CharField(max_length=50, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='medium')

#     def __str__(self):
#         return self.text
#     def set_correct_answer(self, answer):
#         self.correct_answer = answer
#         self.save()


# Question Model
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    difficulty = models.CharField(max_length=50, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='medium')

    def __str__(self):
        return self.text

# Answer Model
class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class QuizProgressManager(models.Manager):
    def get_incomplete_quizzes(self, user):
        return Quiz.objects.filter(progress__user=user, progress__completed=False).distinct()

# Model to track quiz progress      
class QuizProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    quiz = models.ForeignKey(Quiz, related_name='progress', on_delete=models.CASCADE, db_index=True)
    score = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    feedback = models.TextField(blank=True)
    progress = models.IntegerField(default=0)

    @classmethod
    def get_incomplete_quizzes(cls, user):
        return Quiz.objects.filter(progress__user=user, progress__completed=False).distinct().select_related('course')

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

# Model to track course progress
class CourseProgress(models.Model):
    user = models.ForeignKey(User, related_name='course_progress', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='progress', on_delete=models.CASCADE)
    completion_status = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    completed_modules = models.ManyToManyField(Module, blank=True, related_name='completed_progress') 
    completed_content = models.ManyToManyField(Content, blank=True, related_name='completed_progress_content')  
    
    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f'{self.user.username} - {self.course.title}'

# Certificates Model
class Certificate(models.Model):
    user = models.ForeignKey(User, related_name='certificates', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='certificates', on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'Certificate for {self.user.username} - {self.course.title}'

# Content Progress
class ContentProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, related_name='progress', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    viewed = models.BooleanField(default=False)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'content')

# Notification
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='Default Title')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.message}"