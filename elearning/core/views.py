import logging
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, action
from django.utils.decorators import method_decorator
from .models import Course, Content, Module, CourseProgress, QuizProgress, QuestionAnswer, Course, Quiz, Question, Answer
from .serializers import CourseProgressSerializer, QuizProgressSerializer, QuestionAnswerSerializer, QuizSerializer, QuestionSerializer, AnswerSerializer, CourseSerializer, ModuleSerializer, ContentSerializer

logger = logging.getLogger(__name__)

# @csrf_exempt
# @api_view(['POST'])
def index(request):
    return HttpResponse("<h1>Hello</h1>")

# Register View
# @csrf_exempt
@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username = username).exists():
            return Response({"message" : "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password, email=email)
        token, _ = Token.objects.get_or_create(user = user)
        # user.save()
        return Response({"message" : "Registration Successful!", "token" : token.key}, status=status.HTTP_201_CREATED)

# @csrf_exempt
@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user = user)
            return Response({"message" : "Login successful!", "token" : token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"message" : "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# Logout View
@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"message" : "Logout Successful"}, status=status.HTTP_200_OK)

# Create Course View
class CourseCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(instructor = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Update Course View
class CourseUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        if course.instructor != request.user:
            return Response({"error" : "You are not authorized to update this course."})
        
        serializer = CourseSerializer(course, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Course View
class CourseDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        if course.instructor != request.user:
            return Response({"error" : "You are not authorized to delete this course."}, status=status.HTTP_403_FORBIDDEN)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Create Module View
class ModuleCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        logger.info(f'Received request to create module for course_id: {course_id}')
        logger.info(f'Authenticated user: {request.user}')
        course = get_object_or_404(Course, id=course_id)
        logger.info(f'Course instructor: {course.instructor}')
        
        if course.instructor != request.user:
            return Response({"error" : "You are not authorized to add modules to this course."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(course = course)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Update Module View
class ModuleUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        module = get_object_or_404(Module, pk=pk)
        if module.course.instructor != request.user:
            return Response({"error" : "You are not authorized to update this module."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ModuleSerializer(module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Delete Module View
class ModuleDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        module = get_object_or_404(Module, pk=pk)
        if module.course.instructor != request.user:
            return Response({"error" : "You are not authorized to delete this module."}, status=status.HTTP_403_FORBIDDEN)
        module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create Content View
class ContentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, module_id):
        module = get_object_or_404(Module, id=module_id)
        if module.course.instructor != request.user:
            return Response({"error" : "You are not authorized to add content to this module."}, status=status.HTTP_403_FORBIDDEN)
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(module=module)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Content View
class ContentUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        if content.module.course.instructor != request.user:
            return Response({"error" : "You are not authorized to update this content."}, status=status.HTTP_403_FORBIDDEN)
        serializer = ContentSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Content View
class ContentDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        if content.module.course.instructor != request.user:
            return Response({"error" : "You are not authorized to delete this content."}, status=status.HTTP_403_FORBIDDEN)
        content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseProgressView(APIView):
    def get(self, request, course_id):
        progress = get_object_or_404(CourseProgress, user=request.user, course_id=course_id)
        serializer = CourseProgressSerializer(progress)
        return Response(serializer.data)

    def post(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        progress, created = CourseProgress.objects.get_or_create(user=request.user, course=course)
        progress.completed_modules.add(*request.data.get('completed_modules', []))
        progress.completion_status = request.data.get('completion_status', progress.completion_status)
        progress.save()
        serializer = CourseProgressSerializer(progress)
        return Response(serializer.data, status=status.HTTP_200_OK)

class QuizProgressView(APIView):
    def get(self, request, quiz_id):
        progress = get_object_or_404(QuizProgress, user=request.user, quiz_id=quiz_id)
        serializer = QuizProgressSerializer(progress)
        return Response(serializer.data)

    def post(self, request, quiz_id):
        quiz = get_object_or_404(Quiz, id=quiz_id)
        progress, created = QuizProgress.objects.get_or_create(user=request.user, quiz=quiz)
        progress.score = request.data.get('score', progress.score)
        progress.completed = request.data.get('completed', progress.completed)
        progress.completed_at = request.data.get('completed_at', progress.completed_at)
        progress.save()
        serializer = QuizProgressSerializer(progress)
        return Response(serializer.data, status=status.HTTP_200_OK)

class QuestionAnswerView(APIView):
    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        selected_answer = request.data.get('selected_answer')
        is_correct = selected_answer == question.correct_answer
        answer, created = QuestionAnswer.objects.get_or_create(user=request.user, question=question)
        answer.selected_answer = selected_answer
        answer.is_correct = is_correct
        answer.save()
        serializer = QuestionAnswerSerializer(answer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class EvaluateQuizViewSet(viewsets.ViewSet):
    @action(detail=True, methods=['post'])
    def evaluate(self, request, pk=None):
        quiz = self.get_object()
        answers = request.data.get('answers', [])

        if not answers:
            return Response({'error': 'No answers provided'}, status=status.HTTP_400_BAD_REQUEST)

        correct = 0
        total = quiz.questions.count()

        for answer in answers:
            question_id = answer.get('question_id')
            selected_answer_id = answer.get('answer_id')

            question = get_object_or_404(Question, id=question_id)
            answer_obj = get_object_or_404(Answer, id=selected_answer_id)

            if question.correct_answer == answer_obj.id:
                correct += 1

        score_percentage = (correct / total) * 100 if total else 0

        # Save progress or other logic here

        return Response({'score': score_percentage}, status=status.HTTP_200_OK)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizCreateView(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

