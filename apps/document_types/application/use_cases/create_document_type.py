class CreateDocumentType:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, dto):
        document_type = self.repository.create(
            name=dto.name,
            description=dto.description,
            is_active=dto.is_active,
        )
        return document_type
