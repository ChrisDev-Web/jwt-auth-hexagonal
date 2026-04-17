from apps.audit.infrastructure.db.models import AuditEventModel


class DjangoAuditRepository:
    def get_all(self, action=None, session_state=None):
        queryset = AuditEventModel.objects.all().order_by("-created_at")
        if action:
            queryset = queryset.filter(action=action.upper())
        if session_state:
            queryset = queryset.filter(session_state=session_state.upper())
        return queryset
