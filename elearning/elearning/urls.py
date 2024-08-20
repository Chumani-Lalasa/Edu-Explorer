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
]
