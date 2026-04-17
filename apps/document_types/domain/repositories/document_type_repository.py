from abc import ABC, abstractmethod


class DocumentTypeRepository(ABC):
    @abstractmethod
    def create(self, name, description, is_active=True):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, document_type_id):
        pass

    @abstractmethod
    def update(self, document_type_id, **kwargs):
        pass

    @abstractmethod
    def delete(self, document_type_id):
        pass
