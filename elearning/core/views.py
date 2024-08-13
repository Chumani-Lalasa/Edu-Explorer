# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def index(request):
#     return HttpResponse("<h1>Hello</h1>")

# def about(request):
#     return HttpResponse("Hello from about")

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello</h1>")

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if(username == "user" and password == "pass"):
            return Response({"message" : "Login Successfull!"}, status = status.HTTP_200_OK)
        else:
            return Response({"message" : "Invalid Credentials"}, status = status.HTTP_401_UNAUTHORIZED)
