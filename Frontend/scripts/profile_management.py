import json

class ProfileManager:
    def __init__(self):
        self.profiles = {}  # User profiles stored as {username: {name, email, password}}

    def create_profile(self, username, name, email, password):
        self.profiles[username] = {"name": name, "email": email, "password": password}
        return f"Profile created for {username}"

    def view_profile(self, username):
        profile = self.profiles.get(username)
        if profile:
            return f"Name: {profile['name']}\nEmail: {profile['email']}"
        return "Profile not found"

    def update_profile(self, username, name=None, email=None, password=None):
        profile = self.profiles.get(username)
        if profile:
            if name: profile['name'] = name
            if email: profile['email'] = email
            if password: profile['password'] = password
            return "Profile updated successfully"
        return "Profile not found"
