from abc import ABC, abstractmethod


class AuditRepository(ABC):
    @abstractmethod
    def get_all(self, action=None, session_state=None):
        pass
