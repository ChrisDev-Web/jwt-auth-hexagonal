from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6)


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6, write_only=True)
    username = serializers.CharField(required=False, allow_blank=True, max_length=150)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()