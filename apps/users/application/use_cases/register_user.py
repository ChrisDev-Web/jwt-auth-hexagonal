from apps.users.domain.exceptions.auth_exceptions import UserAlreadyExists


class RegisterUser:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self, dto):
        existing_user = self.user_repo.get_by_email(dto.email)
        if existing_user:
            raise UserAlreadyExists()

        username = dto.username or dto.email.split("@")[0]

        user = self.user_repo.create(
            email=dto.email,
            password=dto.password,
            username=username,
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        return {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser,
        }
