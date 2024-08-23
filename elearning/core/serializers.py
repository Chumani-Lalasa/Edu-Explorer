from rest_framework import serializers
from .models import Course, Module, Content

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

