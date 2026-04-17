from apps.users.infrastructure.db.models import UserSessionModel, UserModel
from django.db import transaction
from django.utils import timezone


class DjangoSessionRepository:

    @transaction.atomic
    def create_session(self, user_id, ip, user_agent):
        try:
            user = UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return None

        return UserSessionModel.objects.create(
            user=user,
            ip_address=ip,
            user_agent=user_agent
        )

    @transaction.atomic
    def close_latest_active_session(self, user_id):
        session = (
            UserSessionModel.objects.filter(user_id=user_id, is_active=True)
            .order_by("-created_at")
            .first()
        )
        if not session:
            return None
        session.is_active = False
        session.ended_at = timezone.now()
        session.save()
        return session