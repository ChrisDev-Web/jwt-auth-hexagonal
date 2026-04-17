class InvalidCredentials(Exception):
    pass

class UserNotFound(Exception):
    pass

class UserInactive(Exception):
    pass

class TooManyAttempts(Exception):
    pass

class UserAlreadyExists(Exception):
    pass