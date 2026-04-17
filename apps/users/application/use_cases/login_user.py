from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from datetime import timedelta

from apps.users.domain.exceptions.auth_exceptions import InvalidCredentials


class LoginUser:

    def __init__(self, user_repo, token_repo, session_repo):
        self.user_repo = user_repo
        self.token_repo = token_repo
        self.session_repo = session_repo

    def execute(self, dto):

        user = self.user_repo.get_by_email(dto.email)

        if not user:
            raise InvalidCredentials()

        if not user.is_active:
            raise InvalidCredentials()

        if not check_password(dto.password, user.password):
            raise InvalidCredentials()

        # 🔥 AQUÍ ESTÁ EL FIX CLAVE
        refresh = RefreshToken.for_user(user)  # ahora SÍ es Django UserModel

        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        if hasattr(self.token_repo, "revoke_all_user_tokens"):
            self.token_repo.revoke_all_user_tokens(user.id)

        self.token_repo.save_access_token(
            user.id,
            access_token,
            timezone.now() + timedelta(minutes=15)
        )

        self.token_repo.save_refresh_token(
            user.id,
            refresh_token,
            timezone.now() + timedelta(days=7)
        )

        session = self.session_repo.create_session(
            user.id,
            dto.ip,
            dto.user_agent
        )

        return {
            "user_id": user.id,
            "access": access_token,
            "refresh": refresh_token,
            "session_started_at": session.created_at if session else None,
        }