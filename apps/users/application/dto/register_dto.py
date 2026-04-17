import re


class RegisterDTO:
    def __init__(self, email, password, username=None):
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email")

        if not password or len(password) < 6:
            raise ValueError("Password must have at least 6 chars")

        self.email = email
        self.password = password
        self.username = username
