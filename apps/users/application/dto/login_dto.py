import re

class LoginDTO:
    def __init__(self, email, password, ip, user_agent):
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email")

        if not password:
            raise ValueError("Password required")

        self.email = email
        self.password = password
        self.ip = ip
        self.user_agent = user_agent