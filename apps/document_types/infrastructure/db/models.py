from django.db import models
from django.utils import timezone


class DocumentTypeModel(models.Model):
    name = models.CharField(max_length=120, db_index=True)
    description = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True, db_index=True)
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "document_types"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_active:
            self.deleted_at = None
        elif self.deleted_at is None:
            self.deleted_at = timezone.now()
        super().save(*args, **kwargs)
