from rest_framework import serializers
from .models import Course, Module, Content, Notification
from .models import UserProfile, Question, Quiz, Lesson ,CourseProgress, QuizProgress, QuestionAnswer, Answer, ContentProgress

# UserProfile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

# Course Serializer
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'instructor', 'name', 'duration']
        read_only_fields = ['id', 'created_at', 'updated_at', 'instructor']

# Module Serializer
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'course', 'title', 'description', 'order']
        read_only_fields = ['course']

# Content Serializer
class ContentSerializer(serializers.ModelSerializer):
    module = serializers.PrimaryKeyRelatedField(queryset=Module.objects.all(), required=True)
    class Meta:
        model = Content
        fields = ['id', 'module', 'content_type', 'text', 'file', 'order']

# Lesson Serializer
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'course', 'progress', 'lesson_type', 'category']

# Course Progress Serializer
class CourseProgressSerializer(serializers.ModelSerializer):
    completed_content = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    completed_modules = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = CourseProgress
        fields = ['user', 'course', 'completed_modules', 'completion_status', 'started_at', 'completed_at', 'completed_content']

# Quiz Serializer
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

# Quiz Progress Serializer
class QuizProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizProgress
        fields = ['user', 'quiz', 'score', 'completed', 'completed_at', 'feedback']

#Question Answer Serializer
class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = ['user', 'question', 'selected_answer', 'is_correct']

# Question Serializer
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

# Answer Serializer
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class ContentProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentProgress
        fields = ['content', 'completed', 'viewed_at']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'message', 'is_read', 'created_at']


