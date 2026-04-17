from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    email = models.EmailField(unique=True, db_index=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class AccessTokenModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, db_index=True)
    token = models.TextField()
    is_revoked = models.BooleanField(default=False, db_index=True)
    expires_at = models.DateTimeField(db_index=True)


class RefreshTokenModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, db_index=True)
    token = models.TextField()
    is_revoked = models.BooleanField(default=False, db_index=True)
    expires_at = models.DateTimeField(db_index=True)


class UserSessionModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, db_index=True)
    ip_address = models.CharField(max_length=45)
    user_agent = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    ended_at = models.DateTimeField(null=True, blank=True, db_index=True)