from rest_framework import serializers
from .models import Course, Module, Content
from .models import CourseProgress, QuizProgress, QuestionAnswer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'instructor']
        read_only_fields = ['id', 'created_at', 'updated_at', 'instructor']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['course', 'title', 'description', 'order']

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'module', 'content_type', 'text', 'file', 'order']

class CourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProgress
        fields = ['user', 'course', 'completed_modules', 'completion_status', 'started_at', 'completed_at']

class QuizProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizProgress
        fields = ['user', 'quiz', 'score', 'completed', 'completed_at']

class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = ['user', 'question', 'selected_answer', 'is_correct']