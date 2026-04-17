from apps.document_types.domain.exceptions.document_type_exceptions import DocumentTypeNotFound


class DeleteDocumentType:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, document_type_id):
        deleted = self.repository.delete(document_type_id)
        if not deleted:
            raise DocumentTypeNotFound()
        return deleted
