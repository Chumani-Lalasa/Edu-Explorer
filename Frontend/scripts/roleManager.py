class RoleManager:
    def __init__(self):
        self.roles = {'admin': ['add_course', 'delete_course', 'view_courses'],
                      'moderator': ['add_course', 'view_courses'],
                      'user': ['view_courses']}

    def check_permission(self, user_role, action):
        if action in self.roles.get(user_role, []):
            return True
        return False

# Sample Usage
role_manager = RoleManager()
print(role_manager.check_permission("admin", "delete_course"))  # Should return True

