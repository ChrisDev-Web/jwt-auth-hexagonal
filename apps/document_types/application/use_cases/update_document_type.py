from apps.document_types.domain.exceptions.document_type_exceptions import DocumentTypeNotFound


class UpdateDocumentType:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, document_type_id, dto):
        updated = self.repository.update(
            document_type_id,
            name=dto.name,
            description=dto.description,
            is_active=dto.is_active,
        )
        if not updated:
            raise DocumentTypeNotFound()
        return updated
