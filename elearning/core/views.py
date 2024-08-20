from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from .models import Course
from .serializers import CourseSerializer

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