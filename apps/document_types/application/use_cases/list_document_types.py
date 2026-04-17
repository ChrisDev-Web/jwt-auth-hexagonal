class ListDocumentTypes:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, is_active=True):
        return self.repository.get_all(is_active=is_active)
