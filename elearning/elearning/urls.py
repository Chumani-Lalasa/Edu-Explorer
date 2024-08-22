"""
URL configuration for elearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/register', views.RegisterView.as_view(), name="register"), 
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/logout', views.LogoutView.as_view(), name='logout'),
    path('api/courses/create/', views.CourseCreateView.as_view(), name='course-create'),
    path('api/courses/<int:pk>/update/', views.CourseUpdateView.as_view(), name='course-update'),
    path('api/courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course-delete'),

    path('api/courses/<int:course_id>/modules/create/', views.ModuleCreateView.as_view(), name='module-create'),
    path('api/modules/<int:pk>/update/', views.ModuleUpdateview.as_view(), name='module-update'),
    path('api/modules/<int:pk>/delete', views.ModuleDeleteView.as_view(), name='module-delete'),
    path('api/modules/<int:module_id>/contents/create/', views.ContentCreateView.as_view(), name='content-create'),
    path('api/contents/<int:pk>/update/', views.ContentUpdateView.as_view(), name='content-update'),
    path('api/contents/<int:pk>/delete/', views.ContentDeleteView.as_view(), name='content-delete'),

    path('progress/course/<int:course_id>/', views.CourseProgressView.as_view(), name='course-progress'),
    path('progress/quiz/<int:quiz_id>/', views.QuizProgressView.as_view(), name='quiz-progress'),
    path('progress/question/<int:question_id>/answer/', views.QuestionAnswerView.as_view(), name='question-answer'),
]
