import hashlib

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, entered_password):
        return self.password == hashlib.sha256(entered_password.encode()).hexdigest()

# Sample Usage
admin = Admin("admin", "securepassword")
print(admin.check_password("wrongpassword"))  # Should return False
