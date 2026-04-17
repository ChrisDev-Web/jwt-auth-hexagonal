from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    def create(self, user):
        pass