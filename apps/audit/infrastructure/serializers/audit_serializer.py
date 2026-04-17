from rest_framework import serializers


class AuditOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = serializers.IntegerField(allow_null=True)
    user_email = serializers.CharField(allow_blank=True)
    action = serializers.CharField()
    message = serializers.CharField()
    entity_type = serializers.CharField()
    entity_id = serializers.IntegerField(allow_null=True)
    entity_name = serializers.CharField()
    session_state = serializers.CharField(allow_blank=True)
    session_started_at = serializers.DateTimeField(allow_null=True)
    session_ended_at = serializers.DateTimeField(allow_null=True)
    created_at = serializers.DateTimeField()
