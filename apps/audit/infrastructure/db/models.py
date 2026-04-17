from django.conf import settings
from django.db import models


class AuditEventModel(models.Model):
    ACTION_CHOICES = (
        ("LOGIN", "LOGIN"),
        ("LOGOUT", "LOGOUT"),
        ("REGISTER", "REGISTER"),
        ("CREATE", "CREATE"),
        ("UPDATE", "UPDATE"),
        ("DELETE", "DELETE"),
    )
    SESSION_STATE_CHOICES = (
        ("ACTIVE", "ACTIVE"),
        ("INACTIVE", "INACTIVE"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES, db_index=True)
    message = models.CharField(max_length=255)
    entity_type = models.CharField(max_length=100, blank=True, default="")
    entity_id = models.PositiveBigIntegerField(null=True, blank=True)
    entity_name = models.CharField(max_length=150, blank=True, default="")
    session_state = models.CharField(max_length=10, choices=SESSION_STATE_CHOICES, blank=True, default="")
    session_started_at = models.DateTimeField(null=True, blank=True)
    session_ended_at = models.DateTimeField(null=True, blank=True)
    ip_address = models.CharField(max_length=45, blank=True, default="", db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = "audit_events"
