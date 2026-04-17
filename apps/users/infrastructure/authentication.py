from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.users.infrastructure.repositories.django_token_repository import DjangoTokenRepository


class DatabaseBackedJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        auth_result = super().authenticate(request)
        if auth_result is None:
            return None

        user, validated_token = auth_result
        raw_token = str(validated_token)
        token_repo = DjangoTokenRepository()

        if not token_repo.is_token_valid(raw_token):
            raise AuthenticationFailed("Token revoked or not recognized")

        return user, validated_token
