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
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='course')
router.register(r'quizzes', views.EvaluateQuizViewSet, basename='quiz')
router.register(r'questions', views.QuestionViewSet, basename='question')

question_list = views.QuestionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
question_detail = views.QuestionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/register/', views.RegisterView.as_view(), name="register"),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/logout/', views.LogoutView.as_view(), name='logout'),
    path('api/courses/create/', views.CourseCreateView.as_view(), name='course-create'),
    path('api/courses/<int:pk>/update/', views.CourseUpdateView.as_view(), name='course-update'),
    path('api/courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course-delete'),
    path('api/courses/', views.CourseListView.as_view(), name='course-list'),

    # Modules and contents
    path('api/courses/<int:course_id>/modules/create/', views.ModuleCreateView.as_view(), name='module-create'),
    path('api/modules/<int:pk>/update/', views.ModuleUpdateView.as_view(), name='module-update'),
    path('api/modules/<int:pk>/delete/', views.ModuleDeleteView.as_view(), name='module-delete'),
    path('api/modules/<int:module_id>/contents/create/', views.ContentCreateView.as_view(), name='content-create'),
    path('api/contents/<int:pk>/update/', views.ContentUpdateView.as_view(), name='content-update'),
    path('api/contents/<int:pk>/delete/', views.ContentDeleteView.as_view(), name='content-delete'),

    # Lessons management
    path('api/modules/<int:module_id>/lessons/create/', views.LessonCreateView.as_view(), name='lesson-create'),
    path('api/lessons/<int:pk>/update/', views.LessonUpdateView.as_view(), name='lesson-update'),
    path('api/lessons/<int:pk>/delete/', views.LessonDeleteView.as_view(), name='lesson-delete'),
    # path('api/lessons/<int:pk>/', views.LessonDetailView.as_view(), name='lesson-detail'),
    path('api/modules/<int:module_id>/lessons/', views.LessonListView.as_view(), name='lesson-list'),

    # Progress tracking
    path('api/progress/course/<int:course_id>/', views.CourseProgressView.as_view(), name='course-progress'),
    path('api/progress/quiz/<int:quiz_id>/', views.QuizProgressView.as_view(), name='quiz-progress'),
    path('progress/question/<int:question_id>/answer/', views.QuestionAnswerView.as_view(), name='question-answer'),
    path('api/content/<int:content_id>/progress/', views.ContentProgressView.as_view(), name='content-progress'),

    # Questions
    path('api/questions/', question_list, name='question-list'),
    path('api/questions/<int:pk>/', question_detail, name='question-detail'), 

    # Quizzes
    path('api/quizzes/', views.QuizListCreateView.as_view(), name='quiz-list'),
    path('api/quizzes/<int:pk>/', views.QuizDetailView.as_view(), name='quiz-detail'),
    path('api/quizzes/<int:course_id>/create/', views.QuizCreateView.as_view(), name='quiz-create'),
    path('api/quizzes/<int:pk>/evaluate/', views.EvaluateQuizViewSet.as_view({'post': 'evaluate'}), name='evaluate-quiz'),

    # Router URLs
    path('', include(router.urls)),

    # JWT Token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Content Progress
    path('api/content/<int:content_id>/complete/', views.MarkContentCompleteView.as_view(), name='content-complete'),
    path('api/content/<int:content_id>/progress/', views.ContentProgressView.as_view(), name='content-progress'),

    # Notification
    path('api/notifications/', views.NotificationListView.as_view(), name='notification-list'),
    path('api/notifications/create/', views.NotificationCreateView.as_view(), name='notification-create'), 
    path('api/notifications/<int:pk>/read/', views.NotificationReadView.as_view(), name='notification-read'),

    # Lessons based on user preferences
    path('courses/<int:course_id>/lessons/', views.LessonListView.as_view(), name='course-lessons'),
]
