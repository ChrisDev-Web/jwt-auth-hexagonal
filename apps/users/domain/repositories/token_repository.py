from abc import ABC, abstractmethod

class TokenRepository(ABC):

    @abstractmethod
    def revoke_token(self, token):
        pass

    @abstractmethod
    def is_token_revoked(self, token):
        pass

    @abstractmethod
    def blacklist_token(self, token):
        pass
    
    @abstractmethod
    def is_blacklisted(self, token):
        pass