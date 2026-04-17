from apps.document_types.domain.exceptions.document_type_exceptions import DocumentTypeNotFound


class GetDocumentType:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, document_type_id):
        document_type = self.repository.get_by_id(document_type_id)
        if not document_type:
            raise DocumentTypeNotFound()
        return document_type
