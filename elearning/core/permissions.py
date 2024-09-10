from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.userprofile.role == 'admin'
    
class IsInstructorUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.userprofile.role == 'instructor'

class IsStudentUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.userprofile.role == 'student'