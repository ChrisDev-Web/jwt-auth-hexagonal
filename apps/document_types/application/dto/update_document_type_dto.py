class UpdateDocumentTypeDTO:
    def __init__(self, name=None, description=None, is_active=None):
        self.name = name
        self.description = description
        self.is_active = is_active
