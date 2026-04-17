class DocumentType:
    def __init__(self, id, name, description, is_active=True, deleted_at=None):
        self.id = id
        self.name = name
        self.description = description
        self.is_active = is_active
        self.deleted_at = deleted_at
