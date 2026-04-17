from apps.audit.infrastructure.db.models import AuditEventModel
from apps.users.infrastructure.db.models import UserModel


def _get_user(user_id=None, user=None):
    if user is not None and getattr(user, "is_authenticated", False):
        return user
    if user_id is not None:
        return UserModel.objects.filter(id=user_id).first()
    return None


def log_session_login(user_id, session_started_at, ip_address=""):
    user = _get_user(user_id=user_id)
    if not user:
        return
    AuditEventModel.objects.create(
        user=user,
        action="LOGIN",
        message="Inicio sesion en el sistema",
        session_state="ACTIVE",
        session_started_at=session_started_at,
        ip_address=ip_address,
    )


def log_session_logout(user_id, session_started_at, session_ended_at, ip_address=""):
    user = _get_user(user_id=user_id)
    if not user:
        return
    event = (
        AuditEventModel.objects.filter(
            user=user,
            action="LOGIN",
            session_state="ACTIVE",
        )
        .order_by("-created_at")
        .first()
    )
    if event:
        event.session_state = "INACTIVE"
        event.session_ended_at = session_ended_at
        if ip_address:
            event.ip_address = ip_address
        event.save()
    else:
        AuditEventModel.objects.create(
            user=user,
            action="LOGOUT",
            message="Cerro sesion en el sistema",
            session_state="INACTIVE",
            session_started_at=session_started_at,
            session_ended_at=session_ended_at,
            ip_address=ip_address,
        )


def log_user_registered(user_id, email, ip_address=""):
    user = _get_user(user_id=user_id)
    AuditEventModel.objects.create(
        user=user,
        action="REGISTER",
        message="Usuario registrado en el sistema",
        entity_type="User",
        entity_id=user_id,
        entity_name=email,
        ip_address=ip_address,
    )


def log_record_action(user, action, entity_type, entity_id, entity_name, message, ip_address=""):
    target_user = _get_user(user=user)
    AuditEventModel.objects.create(
        user=target_user,
        action=action,
        message=message,
        entity_type=entity_type,
        entity_id=entity_id,
        entity_name=entity_name,
        ip_address=ip_address,
    )
