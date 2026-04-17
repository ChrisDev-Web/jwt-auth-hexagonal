from apps.users.infrastructure.db.models import UserModel
from apps.users.domain.entities.user import User


class DjangoUserRepository:

    def get_by_email(self, email):
        try:
            return UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None

    def create(self, email, password, username, is_staff=False, is_superuser=False, is_active=True):
        return UserModel.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )