from rest_framework_simplejwt.tokens import RefreshToken


class LogoutUser:
    def __init__(self, token_repo, session_repo):
        self.token_repo = token_repo
        self.session_repo = session_repo

    def execute(self, refresh_token):
        token = RefreshToken(refresh_token)
        user_id = token["user_id"]
        revoked = self.token_repo.revoke_refresh_token(refresh_token)
        self.token_repo.revoke_all_user_tokens(user_id)
        session = self.session_repo.close_latest_active_session(user_id)
        return {
            "user_id": user_id,
            "refresh_revoked": bool(revoked),
            "session_closed": bool(session),
            "session_started_at": session.created_at if session else None,
            "session_ended_at": session.ended_at if session else None,
        }
