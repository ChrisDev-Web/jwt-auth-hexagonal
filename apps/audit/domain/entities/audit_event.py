class AuditEvent:
    def __init__(
        self,
        id,
        user_id,
        action,
        message,
        entity_type="",
        entity_id=None,
        entity_name="",
        session_state="",
        session_started_at=None,
        session_ended_at=None,
        created_at=None,
    ):
        self.id = id
        self.user_id = user_id
        self.action = action
        self.message = message
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.session_state = session_state
        self.session_started_at = session_started_at
        self.session_ended_at = session_ended_at
        self.created_at = created_at
