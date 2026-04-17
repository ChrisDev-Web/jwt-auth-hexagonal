from apps.document_types.infrastructure.db.models import DocumentTypeModel


class DjangoDocumentTypeRepository:
    def create(self, name, description, is_active=True):
        return DocumentTypeModel.objects.create(
            name=name,
            description=description,
            is_active=is_active,
        )

    def get_all(self, is_active=True):
        return DocumentTypeModel.objects.filter(is_active=is_active).order_by("id")

    def get_by_id(self, document_type_id):
        try:
            return DocumentTypeModel.objects.get(id=document_type_id)
        except DocumentTypeModel.DoesNotExist:
            return None

    def update(self, document_type_id, **kwargs):
        document_type = self.get_by_id(document_type_id)
        if not document_type:
            return None

        for field_name, field_value in kwargs.items():
            if field_value is not None:
                setattr(document_type, field_name, field_value)

        document_type.save()
        return document_type

    def delete(self, document_type_id):
        document_type = self.get_by_id(document_type_id)
        if not document_type:
            return None
        document_type.is_active = False
        document_type.save()
        return document_type
