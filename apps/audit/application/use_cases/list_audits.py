class ListAudits:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, action=None, session_state=None):
        return self.repository.get_all(action=action, session_state=session_state)
