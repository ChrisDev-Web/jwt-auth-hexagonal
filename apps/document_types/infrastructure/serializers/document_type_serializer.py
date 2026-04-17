from rest_framework import serializers


class CreateDocumentTypeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    description = serializers.CharField(required=False, allow_blank=True, default="")
    is_active = serializers.BooleanField(required=False, default=True)


class UpdateDocumentTypeSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=120)
    description = serializers.CharField(required=False, allow_blank=True)
    is_active = serializers.BooleanField(required=False)


class DocumentTypeOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()
    deleted_at = serializers.DateTimeField(allow_null=True)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
