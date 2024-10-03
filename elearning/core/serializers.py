from rest_framework import serializers
from .models import Course, Module, Content, Notification
from .models import UserProfile, Question, Quiz, Lesson ,CourseProgress, QuizProgress, QuestionAnswer, Answer, ContentProgress
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

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



# Lesson Serializer
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'course', 'progress', 'lesson_type', 'category', 'order']

# Course Progress Serializer
class CourseProgressSerializer(serializers.ModelSerializer):
    completed_content = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    completed_modules = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = CourseProgress
        fields = ['user', 'course', 'completed_modules', 'completion_status', 'started_at', 'completed_at', 'completed_content']

# Answer Serializer
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['text', 'difficulty', 'answers']

    def create(self, validated_data):
        answers_data = validated_data.pop('answers', [])  # Extract answers from validated data
        question = Question.objects.create(**validated_data)  # Create the question
        # Loop through the answers and create them, linking to the created question
        for answer_data in answers_data:
            Answer.objects.create(question=question, **answer_data)
        return question
    
# Quiz Serializer
class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['title', 'description', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions', [])  # Get questions data
        quiz = Quiz.objects.create(**validated_data)  # Create the quiz
        for question_data in questions_data:
            QuestionSerializer().create({**question_data, 'quiz': quiz})  # Create each question
            # question.quiz = quiz  # Set the quiz for the question
            # question.save()  # Save the question with the quiz association
            # question = Question.objects.create(quiz=quiz, **question_data)
        return quiz

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

# Content Serializer
class ContentSerializer(serializers.ModelSerializer):
    module = serializers.PrimaryKeyRelatedField(queryset=Module.objects.all(), required=True)
    lesson = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all(), required=True)
    quiz = QuizSerializer(required=False)  # Accepting raw quiz data as JSON for flexibility

    class Meta:
        model = Content
        fields = ['id', 'lesson', 'module', 'content_type', 'text', 'file', 'order', 'video_url', 'quiz']

    def validate_video_url(self, value):
        if value:
            validate = URLValidator()
            try:
                validate(value)
            except ValidationError:
                raise serializers.ValidationError("Enter a valid URL.")
        return value

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        quiz_data = validated_data.pop('quiz', None)  # Get the quiz data if provided
        content = Content.objects.create(**validated_data)  # Create the content instance
        
        if quiz_data:
            # Create the Quiz instance first
            quiz_instance = QuizSerializer().create({**quiz_data, 'content': content})

        return content

class ContentProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentProgress
        fields = ['content', 'completed', 'viewed_at']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'message', 'is_read', 'created_at']


