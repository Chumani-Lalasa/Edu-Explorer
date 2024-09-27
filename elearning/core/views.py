import logging
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, exceptions
from rest_framework.exceptions import NotFound, APIException
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
# from django_ratelimit.decorators import ratelimit
from rest_framework.decorators import api_view, action
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import Course, Content, Module, CourseProgress, QuizProgress, QuestionAnswer, Course, Quiz, Question, Answer, ContentProgress, Notification, Lesson
from .serializers import CourseProgressSerializer, QuizProgressSerializer, QuestionAnswerSerializer, QuizSerializer, QuestionSerializer, AnswerSerializer, CourseSerializer, ModuleSerializer, ContentSerializer, ContentProgressSerializer, NotificationSerializer, LessonSerializer
from rest_framework.throttling import UserRateThrottle
from .permissions import IsAdminUser, IsInstructorUser, IsStudentUser
from .utils import check_incomplete_content, check_incomplete_quizzes
from rest_framework.generics import ListAPIView
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

        if not username or not password or not email:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if len(password) < 8:
            return Response({"error": "Password must be at least 8 characters long"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username = username).exists():
            return Response({"message" : "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            token, _ = Token.objects.get_or_create(user = user)
            # user.save()
            return Response({"message" : "Registration Successful!", "token" : token.key}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Registration error: {e}")
            return Response({"error": "Failed to register user"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @csrf_exempt
@method_decorator(csrf_exempt, name='dispatch')
# @method_decorator(ratelimit(key='ip', rate='5/m', method='POST', block=True), name='post')
# @method_decorator(ratelimit(key='ip', rate='5/m', method='POST', block=True), name='post')
class LoginView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [UserRateThrottle]

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
        try:
            serializer = CourseSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(instructor = request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# Update Course View
class CourseUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            course = get_object_or_404(Course, pk=pk)
            if course.instructor != request.user:
                return Response({"error" : "You are not authorized to update this course."})
            
            serializer = CourseSerializer(course, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Update error: {e}")
            return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Delete Course View
class CourseDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, course_id):
        try:
            course = get_object_or_404(Course, id=course_id)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error fetching course detail: {e}")
            return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        if course.instructor != request.user:
            return Response({"error" : "You are not authorized to delete this course."}, status=status.HTTP_403_FORBIDDEN)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseDetailView(APIView):
    def get(self, request, course_id):
        course = get_object_or_404(Course.objects.only('id', 'title', 'description'), id=course_id)
        serializer = CourseSerializer(course)
        return Response(serializer.data) 

# Pagination class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PaginationError(APIException):
    status_code = 400
    default_detail = "Invalid pagination parameters."

class CourseListView(APIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        logger.info(f"Course list requested by user {request.user}")
        try:
            return super().get(request, *args, **kwargs)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error fetching course list: {e}")
            return Response({"error": "Unable to retrieve courses at the moment"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # courses = Course.objects.select_related('instructor').all()
        # serializer = CourseSerializer(courses, many=True)
        # return Response(serializer.data)

class CourseModuleListView(APIView):
    def get(self, request, course_id):
        course = get_object_or_404(Course.objects.prefetch_related('modules'), id=course_id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

class CourseSearchView(APIView):
    def get(self, request):
        search_term = request.query_params.get('search', '')
        courses = Course.objects.filter(title_icontains=search_term).only('id', 'title', 'description')
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

# Create Module View
class ModuleCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        logger.info(f'Received request to create module for course_id: {course_id}')
        logger.info(f'Authenticated user: {request.user}')
        course = get_object_or_404(Course, id=course_id)
        logger.info(f'Course instructor: {course.instructor}')
        
        # if course.instructor != request.user:
        #     return Response({"error" : "You are not authorized to add modules to this course."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(course=course)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f'Serializer errors: {serializer.errors}')  # Log errors for debugging
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
# Update Module View
class ModuleUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        module = get_object_or_404(Module, pk=pk)
        if module.course.instructor != request.user:
            return Response({"error" : "You are not authorized to update this module."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ModuleSerializer(module, data=request.data, partial = True)
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
        serializer = ContentSerializer(content, data=request.data, partial = True)
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

class ContentProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, content_id):
        user = request.user
        content = get_object_or_404(Content, id=content_id)

        try:
            progress = ContentProgress.objects.get(user=user, content=content)
        except ContentProgress.DoesNotExist:
            return Response({"message": "Content progress not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContentProgressSerializer(progress)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, content_id):
        content = get_object_or_404(Content, id=content_id)
        viewed = request.data.get('viewed', False)

        # Update or create the progress record
        progress, created = ContentProgress.objects.update_or_create(
            user=request.user,
            content=content,
            defaults={'viewed': viewed}
        )

        return Response({"message": "Progress updated successfully", "viewed": viewed}, status=status.HTTP_200_OK)

    def mark_content_as_viewed(request, content_id):
        content = get_object_or_404(Content, id=content_id)
        content_progress, created = ContentProgress.objects.get_or_create(
            user=request.user, content=content
        )
        content_progress.viewed = True
        content_progress.save()

        return Response({'viewed': True}, status=status.HTTP_200_OK)

def check_incomplete_content(user, course_id):
    # Logic to find incomplete content for the user's course
    course_progress = get_object_or_404(CourseProgress, user=user, course_id=course_id)
    all_content = Content.objects.filter(module__course_id=course_id)
    completed_content_ids = course_progress.completed_content.values_list('id', flat=True)
    
    # Filter out completed content
    incomplete_content = all_content.exclude(id__in=completed_content_ids)
    return [{'id': content.id, 'type': content.content_type, 'text': content.text} for content in incomplete_content]

class CourseProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, course_id):
        progress = get_object_or_404(
            CourseProgress.objects.select_related('course', 'user'), 
            user=request.user, 
            course_id=course_id
        )
        incomplete_content = check_incomplete_content(request.user, course_id)
        serializer = CourseProgressSerializer(progress)

        return Response({
            "course": progress.course.id,
            "progress": serializer.data,
            "incomplete_content": incomplete_content
        })

    def post(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        progress, created = CourseProgress.objects.get_or_create(user=request.user, course=course)
        progress.completed_modules.add(*request.data.get('completed_modules', []))
        progress.completion_status = request.data.get('completion_status', progress.completion_status)
        progress.save()
        serializer = CourseProgressSerializer(progress)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@method_decorator(cache_page(60 * 15), name='dispatch')
class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class QuestionAnswerView(APIView):
    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        selected_answer_id = request.data.get('selected_answer')

        # get the selected answer object
        selected_answer = get_object_or_404(Answer, id = selected_answer_id)

        # check if the selected answer is correct
        is_correct = selected_answer.id == question.correct_answer.id

        answer, created = QuestionAnswer.objects.get_or_create(user=request.user, question=question)
        answer.selected_answer = selected_answer.id
        answer.is_correct = is_correct
        answer.save()

        # serialize the response
        serializer = QuestionAnswerSerializer(answer)
        return Response(serializer.data, status=status.HTTP_200_OK)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class QuizProgressView(GenericAPIView):
    queryset = QuizProgress.objects.all()
    serializer_class = QuizProgressSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, quiz_id):
        quiz = get_object_or_404(Quiz, id=quiz_id)
        progress, created = QuizProgress.objects.get_or_create(user=request.user, quiz=quiz)
        
        if created:
            # If a new progress was created, set the details
            progress.score = request.data.get('score', 0)  # Default score if not provided
            progress.completed = request.data.get('completed', False)
            if progress.completed:
                progress.completed_at = request.data.get('completed_at', timezone.now())
            progress.save()
            serializer = QuizProgressSerializer(progress)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # If the progress already exists, consider if you want to return 200 or handle it differently
            return Response({"detail": "Progress already exists."}, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def get(self, request, quiz_id):
        print("Requested Quiz ID:", quiz_id)
        progress = get_object_or_404(QuizProgress, user=request.user, quiz_id=quiz_id)
        incomplete_quizzes = check_incomplete_quizzes(request.user)
        serializer = QuizProgressSerializer(progress)
        return Response({"progress": serializer.data, "incomplete_quizzes": incomplete_quizzes}, status=status.HTTP_200_OK)

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizCreateView(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class EvaluateQuizViewSet(viewsets.ViewSet):
    def get_object(self):
        quiz_id = self.kwargs.get('pk')
        return Quiz.objects.get(pk=quiz_id)
    
    @action(detail=True, methods=['post'])
    def evaluate(self, request, pk=None):
        quiz = self.get_object()
        answers = request.data.get('answers', [])

        if not answers:
            return Response({'error': 'No answers provided'}, status=status.HTTP_400_BAD_REQUEST)

        correct = 0
        total = quiz.question_set.count()

        print("Total Question:", total)

        for answer in answers:
            question_id = answer.get('question_id')
            selected_answer_id = answer.get('answer_id')

            question = get_object_or_404(Question, id=question_id)
            answer_obj = get_object_or_404(Answer, id=selected_answer_id)

            print("Question ID:", question_id, "Selected Answer ID:", selected_answer_id)  # Debug
            print("Correct Answer ID:", question.correct_answer) 

            if answer_obj.is_correct:
                correct += 1
        print("Question Id:", question_id, "Selected Answer Id:", selected_answer_id)
        print("Correct Answer Id:", question.correct_answer)
        print("Correct Answers:", correct)
        score_fraction = (correct / total) if total else 0

        # Save progress or other logic here
        QuizProgress.objects.update_or_create(
            user = request.user,
            quiz=quiz,
            defaults={'score': score_fraction, 'completed': True, 'completed_at': timezone.now()}
        )

        return Response({'score': score_fraction}, status=status.HTTP_200_OK)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected view accessible only by authenticated users"})

class AdminView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({'message': 'This view is only accessible to Admin users'})

class InstructorView(APIView):
    permission_classes = [IsInstructorUser]

    def get(self, request):
        return Response({'message': 'This view is only accessible to Instructor users'})

class StudentView(APIView):
    permission_classes = [IsStudentUser]

    def get(self, request):
        return Response({'message': 'This view is only accessible to Student users'})

class MarkContentCompleteView(APIView):
    def post(self, request, content_id):
        content = get_object_or_404(Content, id=content_id)
        user = request.user

        progress, created = ContentProgress.objects.get_or_create(user = user, content = content)

        progress.completed = True
        progress.save()

        return Response({"message": "Content market as completed"}, status=status.HTTP_200_OK)

class NotificationCreateView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

class NotificationReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        notification = Notification.objects.filter(pk = self.kwargs['pk'], user = self.request.user).first()
        if notification:
            return notification
        raise Http404("Notification not found")

    def update(self, request, *args, **kwargs):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({"message": "Notification marked as read"}, status=status.HTTP_200_OK)

class LessonListView(ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        queryset = Lesson.objects.filter(course_id = course_id)

        # Filtering based on query parameters
        progress = self.request.query_params.get('progress')
        lesson_type = self.request.query_params.get('lesson_type')
        category = self.request.query_params.get('category')

        if progress:
            queryset = queryset.filter(progress = progress)
        if lesson_type:
            queryset = queryset.filter(lesson_type = lesson_type)
        if category:
            queryset = queryset.filter(category = category)
            
        return queryset

