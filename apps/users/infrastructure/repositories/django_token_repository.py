from apps.users.infrastructure.db.models import AccessTokenModel, RefreshTokenModel, UserModel
from django.db import transaction
from django.utils import timezone
import hashlib


class DjangoTokenRepository:

    @transaction.atomic
    def save_access_token(self, user_id, token, expires_at):
        user = UserModel.objects.get(id=user_id)

        hashed_token = hashlib.sha256(token.encode()).hexdigest()

        AccessTokenModel.objects.create(
            user=user,
            token=hashed_token,
            expires_at=expires_at
        )

    @transaction.atomic
    def save_refresh_token(self, user_id, token, expires_at):
        user = UserModel.objects.get(id=user_id)

        hashed_token = hashlib.sha256(token.encode()).hexdigest()

        RefreshTokenModel.objects.create(
            user=user,
            token=hashed_token,
            expires_at=expires_at
        )

    def revoke_all_user_tokens(self, user_id):
        AccessTokenModel.objects.filter(user_id=user_id).update(is_revoked=True)
        RefreshTokenModel.objects.filter(user_id=user_id).update(is_revoked=True)

    def revoke_refresh_token(self, token):
        hashed_token = hashlib.sha256(token.encode()).hexdigest()
        refreshed = RefreshTokenModel.objects.filter(token=hashed_token, is_revoked=False).first()
        if not refreshed:
            return None
        refreshed.is_revoked = True
        refreshed.save()
        return refreshed

    def is_token_valid(self, token):
        hashed_token = hashlib.sha256(token.encode()).hexdigest()

        return AccessTokenModel.objects.filter(
            token=hashed_token,
            is_revoked=False,
            expires_at__gt=timezone.now(),
        ).exists()