class User:
    def __init__(self, id, email, password_hash, is_active=True):
        self.id = id
        self.email = email
        self._password_hash = password_hash
        self.is_active = is_active

    def is_enabled(self):
        return self.is_active