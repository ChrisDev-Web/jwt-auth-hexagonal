from abc import ABC, abstractmethod

class SessionRepository(ABC):

    @abstractmethod
    def delete_session(self, session_id):
        pass