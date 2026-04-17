class CreateDocumentTypeDTO:
    def __init__(self, name, description="", is_active=True):
        if not name:
            raise ValueError("Name is required")

        self.name = name
        self.description = description
        self.is_active = is_active
